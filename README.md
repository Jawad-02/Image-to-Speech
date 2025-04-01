# 🧠 Image-to-Speech Web App for Visually Impaired Users

A lightweight web application designed to help blind or visually impaired users extract and hear text from images. Users can upload an image containing text, and the app will process it using image processing techniques and Optical Character Recognition (OCR), then read it aloud using an offline Text-to-Speech engine.

---

## 🚀 Features

- 📷 Upload any image containing text
- 🧪 Automatic image preprocessing to enhance OCR results
- 🧠 Accurate text extraction using Tesseract OCR
- 🔊 Offline Text-to-Speech using `pyttsx3`
- 🎨 Simple and accessible web interface built with Flask
- ✅ Copy extracted text to clipboard with one click
- 👓 Designed with accessibility in mind

---

## 🛠️ Technologies Used

- Python 3.10
- Flask (Web Framework)
- OpenCV (Image Processing)
- pytesseract (OCR)
- Pillow (Image Handling)
- pyttsx3 (Offline Text-to-Speech)
- Bootstrap 5 (Responsive UI)

---

## 📸 Screenshots

| Original Image | Preprocessed Image |
|----------------|---------------------|
| ![Original Image](images_for_testing/images.jpg) | ![Processed Image](images_for_testing/processed_image.jpg)|

> 💡 The preprocessing step improves OCR accuracy by applying grayscale, thresholding, and noise removal.

---

## 📂 Project Structure


project/  
│  
├── static/
│   └── uploads/                # Uploaded and processed image files                        
├── templates/  
│   └── index.html          # Main Flask template  
├── app.py                  # Flask application  
├── requirements.txt        # Python dependencies  
└── README.md               # Project documentation  


---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/image-to-speech-app.git
cd image-to-speech-app 
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install dependencies

- **Windows:** Download from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract)
- **Linux:**

	```bash
	sudo apt install tesseract-ocr
	```
### 5. Run the app
```bash
	python app.py
```
- Then open your browser at: http://127.0.0.1:5000

## 🔒 Accessibility and Design

This project is built with accessibility in mind:
- High-contrast layout
- Large buttons with icons
- Keyboard-navigable interface
- Minimal visual clutter for screen readers

---

## 💡 Future Improvements
- Add multi-language OCR and speech support
- Support for PDF uploads
- Mobile responsiveness and voice commands

---
## 🤝 Contributors
- 👨‍💻 _[Jawad-02](https://github.com/Jawad-02)_ — Developer, Designer, Visionary

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 🙏 Acknowledgments

-   [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
    
-   [Bootstrap](https://getbootstrap.com/)
    
-   Flask
