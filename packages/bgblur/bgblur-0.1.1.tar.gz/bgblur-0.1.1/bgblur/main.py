import subprocess
import json
import argparse
import os
import math
import cv2
import numpy as np
from PIL import Image, ImageFilter
import uuid
from multiprocessing import Pool, cpu_count
from tqdm import tqdm


def ffprobe_get_info(video_path):
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,sample_aspect_ratio,display_aspect_ratio",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        video_path,
    ]
    result = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
    )
    lines = result.stdout.strip().split("\n")
    width = int(lines[0])
    height = int(lines[1])
    sar_str = lines[2]
    dar_str = lines[3]

    if sar_str == "N/A":
        sar_ratio = 1.0
    else:
        sw, sh = sar_str.split(":")
        sw, sh = int(sw), int(sh)
        sar_ratio = sw / sh if sh != 0 else 1.0

    if dar_str == "N/A":
        dar_ratio = (width * sar_ratio) / height
    else:
        dw, dh = dar_str.split(":")
        dw, dh = int(dw), int(dh)
        dar_ratio = dw / dh

    return width, height, sar_ratio, dar_ratio


def normalize_sar(input_video_path):
    w, h, sar_ratio, dar_ratio = ffprobe_get_info(input_video_path)
    print(
        f"[LOG] Input: {input_video_path}, w={w}, h={h}, SAR={sar_ratio:.4f}, DAR={dar_ratio:.4f}"
    )
    if abs(sar_ratio - 1.0) < 1e-6:
        print("[LOG] SAR is already 1:1, skipping normalization.")
        return input_video_path, w, h, dar_ratio

    new_w = math.ceil((w * sar_ratio) / 2) * 2
    new_h = h if h % 2 == 0 else h + 1
    print(f"[LOG] Normalizing SAR: scale to {new_w}x{new_h}, setsar=1")

    temp_filename = f"temp_sar_normalized_{uuid.uuid4()}.mp4"
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        input_video_path,
        "-vf",
        f"scale={new_w}:{new_h},setsar=1",
        "-c:v",
        "libx264",
        "-crf",
        "18",
        "-preset",
        "fast",
        "-c:a",
        "copy",
        temp_filename,
    ]
    subprocess.run(cmd, check=True)
    print("[LOG] SAR normalization complete.")
    return temp_filename, new_w, new_h, dar_ratio


def get_audio_codec(input_video):
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "a:0",
        "-show_entries",
        "stream=codec_name",
        "-of",
        "json",
        input_video,
    ]
    result = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if result.returncode != 0:
        print("[LOG] No audio stream or ffprobe error.")
        return None
    info = json.loads(result.stdout)
    if "streams" not in info or len(info["streams"]) == 0:
        return None
    codec = info["streams"][0].get("codec_name", None)
    return codec


def extract_audio_same_ext(input_video):
    base, ext = os.path.splitext(input_video)
    audio_temp = f"temp_audio{ext}"

    print(f"[LOG] Trying to extract audio with -c:a copy into {audio_temp}")
    cmd_copy = ["ffmpeg", "-y", "-i", input_video, "-vn", "-c:a", "copy", audio_temp]
    result = subprocess.run(
        cmd_copy, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if result.returncode == 0:
        print("[LOG] Audio extracted without re-encoding:", audio_temp)
        return audio_temp

    print("[LOG] -c:a copy failed. Re-encoding to AAC.")
    cmd_aac = [
        "ffmpeg",
        "-y",
        "-i",
        input_video,
        "-vn",
        "-c:a",
        "aac",
        "-q:a",
        "1",
        audio_temp,
    ]
    result = subprocess.run(
        cmd_aac, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if result.returncode == 0:
        print("[LOG] Audio re-encoded to AAC successfully:", audio_temp)
        return audio_temp

    print("[ERROR] Audio extraction/encoding failed.")
    return None


def merge_video_audio(video, audio, output):
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        video,
        "-i",
        audio,
        "-c:v",
        "copy",
        "-c:a",
        "copy",
        output,
    ]
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if r.returncode == 0:
        print("[LOG] Merged video and audio:", output)
    else:
        print("[ERROR] Merging failed:")
        print(r.stderr)


def read_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = []
    idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append((idx, frame))
        idx += 1
    cap.release()
    return frames, fps


def write_video(frames, output_path, fps, width, height):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    for _, f in frames:
        out.write(f)
    out.release()


def process_frame(task):
    (
        idx,
        frame_bgr,
        x_start,
        x_end,
        y_start,
        y_end,
        out_w,
        out_h,
        radius,
        fg_new_w,
        fg_new_h,
        x_offset,
        y_offset,
    ) = task
    hh, ww = frame_bgr.shape[:2]
    xx_end = min(x_end, ww)
    yy_end = min(y_end, hh)
    w_crop = xx_end - x_start
    h_crop = yy_end - y_start
    if w_crop <= 0 or h_crop <= 0:
        # Invalid crop -> black frame
        print(f"[WARNING] Frame {idx}: invalid crop area")
        return (idx, np.zeros((out_h, out_w, 3), dtype=np.uint8))

    # Crop background
    bg_crop = frame_bgr[y_start:yy_end, x_start:xx_end]
    # Resize background
    bg_resized = cv2.resize(bg_crop, (out_w, out_h), interpolation=cv2.INTER_LINEAR)
    bg_pil = Image.fromarray(cv2.cvtColor(bg_resized, cv2.COLOR_BGR2RGB))
    blurred_bg_pil = bg_pil.filter(ImageFilter.GaussianBlur(radius))
    blurred_bg = cv2.cvtColor(np.array(blurred_bg_pil), cv2.COLOR_RGB2BGR)

    # Resize foreground
    fg_resized = cv2.resize(
        frame_bgr, (fg_new_w, fg_new_h), interpolation=cv2.INTER_LINEAR
    )
    blended = blurred_bg.copy()
    blended[y_offset : y_offset + fg_new_h, x_offset : x_offset + fg_new_w] = fg_resized
    return (idx, blended)


def process_video(input_video, out_w, out_h, radius):
    w, h, sar_ratio, dar_ratio = ffprobe_get_info(input_video)
    print(
        f"[LOG] Video after SAR normalization: w={w},h={h},SAR={sar_ratio:.4f},DAR={dar_ratio:.4f}"
    )

    out_aspect = out_w / out_h
    aspect = w / h

    # Crop calculation
    if aspect > out_aspect:
        # Wide -> crop horizontally
        new_width = int(h * out_aspect)
        x_start = (w - new_width) // 2
        x_end = x_start + new_width
        y_start = 0
        y_end = h
        print("[LOG] Cropping horizontally")
    else:
        # Tall -> crop vertically
        new_height = int(w / out_aspect)
        y_start = (h - new_height) // 2
        y_end = y_start + new_height
        x_start = 0
        x_end = w
        print("[LOG] Cropping vertically")

    print(f"[LOG] Crop coords: x=[{x_start},{x_end}), y=[{y_start},{y_end})")

    # Foreground calculation
    fg_scale = out_h / h
    fg_new_w = int(w * fg_scale)
    fg_new_h = out_h
    x_offset = (out_w - fg_new_w) // 2
    y_offset = 0
    print(
        f"[LOG] Foreground: scale={fg_scale:.4f}, size={fg_new_w}x{fg_new_h}, offset=({x_offset},{y_offset})"
    )

    frames, fps = read_frames(input_video)
    tasks = []
    for idx, frame_bgr in frames:
        tasks.append(
            (
                idx,
                frame_bgr,
                x_start,
                x_end,
                y_start,
                y_end,
                out_w,
                out_h,
                radius,
                fg_new_w,
                fg_new_h,
                x_offset,
                y_offset,
            )
        )

    num_workers = cpu_count()
    print(f"[LOG] Using {num_workers} workers for parallel processing.")
    results = []

    with Pool(num_workers) as pool:
        for res in tqdm(pool.imap(process_frame, tasks), total=len(tasks)):
            results.append(res)

    results = sorted(results, key=lambda x: x[0])
    processed_video = "processed_video.mov"
    write_video(results, processed_video, fps, out_w, out_h)
    return processed_video


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("--radius", type=int, default=50, help="Blur radius")
    parser.add_argument(
        "--final_width", type=int, default=1280, help="Final output width"
    )
    parser.add_argument(
        "--final_height", type=int, default=720, help="Final output height"
    )
    args = parser.parse_args()

    input_video = args.input
    output_video = args.output
    radius = args.radius
    out_w = args.final_width
    out_h = args.final_height

    # 1. SAR normalization (only if needed)
    normalized_video, norm_w, norm_h, dar_ratio = normalize_sar(input_video)

    # 2. Video processing (foreground/background editing) - parallelization & progress display with tqdm
    processed_video = process_video(normalized_video, out_w, out_h, radius)

    # 3. Audio extraction
    audio_file = extract_audio_same_ext(input_video)
    if audio_file is None:
        # No audio
        os.rename(processed_video, output_video)
        print("[LOG] No audio track. Video only.")
        if normalized_video != input_video:
            os.remove(normalized_video)
        return

    # 4. Merge video and audio
    merge_video_audio(processed_video, audio_file, output_video)

    # Delete temporary files
    os.remove(processed_video)
    os.remove(audio_file)
    if normalized_video != input_video:
        os.remove(normalized_video)

    print("[LOG] Done:", output_video)


if __name__ == "__main__":
    main()
