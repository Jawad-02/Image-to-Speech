import cv2
import pytesseract
import pyttsx3
import numpy as np

# Load the image
image = cv2.imread("images1.png")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Reduce noise with slight Gaussian blur
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Otsu’s Thresholding (instead of Adaptive)
_, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Apply slight erosion to remove noise without affecting text
kernel = np.ones((2,2), np.uint8)
processed_image = cv2.erode(thresholded, kernel, iterations=1)

cv2.imwrite("processed_image1.jpg", processed_image)

# Show the processed image
cv2.imshow("original", image)
cv2.imshow("Preprocessed", processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Extract text with OCR
text = pytesseract.image_to_string(processed_image)

# remove unwanted break lines from the text
text = text.replace("\n", " ").replace("\r", "")
print("Extracted Text:", text)

# Convert extracted text to speech
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)
engine.say(text)
engine.runAndWait()

