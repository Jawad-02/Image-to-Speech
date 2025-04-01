import os
import cv2
import pytesseract
import pyttsx3
import numpy as np
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to process image and extract text
def process_image(image_path):
    # Load image
    image = cv2.imread(image_path)
    
    # Preprocessing
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise with slight Gaussian blur
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Apply Otsu’s Thresholding (instead of Adaptive)
    _, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Apply slight erosion to remove noise without affecting text
    kernel = np.ones((2,2), np.uint8)
    processed_image = cv2.erode(thresholded, kernel, iterations=1)

    # Save preprocessed image (for debugging)
    processed_image_path = os.path.join(UPLOAD_FOLDER, "processed_image.jpg")
    cv2.imwrite(processed_image_path, processed_image)

    # Extract text
    extracted_text = pytesseract.image_to_string(processed_image)
    
    extracted_text = extracted_text.replace("\n", " ").replace("\r", "")

    return extracted_text, processed_image_path

# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            # Process image
            extracted_text, processed_image_path = process_image(file_path)

            # Convert text to speech
            text_to_speech(extracted_text)

            return render_template("index.html", text=extracted_text, 
                       original_image=file_path, 
                       processed_image=processed_image_path)

    return render_template("index.html", text=None)

if __name__ == "__main__":
    app.run(debug=True)
