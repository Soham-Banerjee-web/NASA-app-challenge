from flask import Flask, render_template, request
import cv2
import numpy as np
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def detect_change(before_path, after_path):
    # Load both SAR images in grayscale
    before = cv2.imread(before_path, cv2.IMREAD_GRAYSCALE)
    after = cv2.imread(after_path, cv2.IMREAD_GRAYSCALE)

    # Resize both images to same shape
    before = cv2.resize(before, (512, 512))
    after = cv2.resize(after, (512, 512))

    # Apply Gaussian blur to reduce speckle noise
    before_blur = cv2.GaussianBlur(before, (5, 5), 0)
    after_blur = cv2.GaussianBlur(after, (5, 5), 0)

    # Compute absolute difference
    diff = cv2.absdiff(before_blur, after_blur)

    # Normalize to 0–255 and apply threshold
    diff_norm = cv2.normalize(diff, None, 0, 255, cv2.NORM_MINMAX)
    _, mask = cv2.threshold(diff_norm, 30, 255, cv2.THRESH_BINARY)

    # Clean mask (remove small noise)
    kernel = np.ones((3,3), np.uint8)
    mask_clean = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)

    # Create red overlay
    overlay = cv2.cvtColor(after, cv2.COLOR_GRAY2BGR)
    overlay[mask_clean > 0] = [0, 0, 255]

    # Compute % area changed
    change_pixels = np.sum(mask_clean > 0)
    total_pixels = mask_clean.size
    change_percent = (change_pixels / total_pixels) * 100

    # Save result image
    result_filename = f"result_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
    result_path = os.path.join(RESULT_FOLDER, result_filename)
    cv2.imwrite(result_path, overlay)

    # Create text summary
    if change_percent < 1:
        desc = "Minimal change detected — stable terrain."
    elif change_percent < 5:
        desc = "Minor surface variation — possible light melt or soil shift."
    elif change_percent < 15:
        desc = "Moderate change — possible glacier retreat or localized flood."
    else:
        desc = "Severe change detected — possible flood, heavy melt, or landslide region."

    analysis = f"Detected {change_percent:.2f}% change area. {desc}"

    return result_path, analysis


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        before = request.files["before"]
        after = request.files["after"]

        before_path = os.path.join(UPLOAD_FOLDER, before.filename)
        after_path = os.path.join(UPLOAD_FOLDER, after.filename)
        before.save(before_path)
        after.save(after_path)

        result_path, analysis = detect_change(before_path, after_path)

        return render_template(
            "result.html",
            result_image=result_path,
            analysis=analysis
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
