# **License Plate Detection Using OpenCV, EasyOCR & Tesseract** 🚗🔍  

## **🔹 Overview**  
This project detects and extracts text from license plates using OpenCV for image processing, Haarcascade for plate detection, and OCR engines like **EasyOCR** and **Tesseract** for text recognition. The backend is powered by **Flask**, making it easy to integrate into a web application.  

---

## **🔹 Technology Stack**  

### 1️⃣ **OpenCV (cv2)**
- Used for image processing and detection of license plates.
- Utilizes **Haarcascade Classifier** to detect plates in images.

### 2️⃣ **Haarcascade Classifier**  
- A pre-trained XML file (`haarcascade_russian_plate_number.xml`) that detects license plates based on patterns.  
- Used to **detect** the location of the license plate in the image.
- Download it from [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades) or download the XML file from this repository.

### 3️⃣ **EasyOCR**  
- Deep learning-based Optical Character Recognition (OCR).  
- Works well on images with **low quality, varying fonts, and multiple languages**.  
- Faster and more accurate than Tesseract for many cases.

### 4️⃣ **Tesseract OCR**  
- Open-source OCR engine from Google.  
- Used as a backup to **EasyOCR** for extracting license plate numbers.  
- Configured to recognize only letters and numbers.
- Download Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki).  

### 5️⃣ **Flask (for Web API)**  
- Serves as the backend for this application.  
- Provides an endpoint to upload images and extract text from detected plates.

---

## **🔹 Installation**  

### **Step 1: Clone the Repository**  
```sh
git clone https://github.com/your-username/license-plate-recognition.git
cd license-plate-recognition
```

### **Step 2: Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **Step 3: Run the Flask App**  
```sh
python app.py
```
By default, it runs on **`http://127.0.0.1:5000/`**.

---

## **🔹 How It Works?**  

1. **Image Preprocessing**
   - Converts the input image to grayscale.
   - Detects the license plate using **Haarcascade**.

2. **OCR Processing**
   - Crops the detected license plate.
   - Extracts text using **EasyOCR**, that extracts the text using deep learning-based models.  
   - **Tesseract OCR** serves as a backup in case EasyOCR fails.  

3. **Flask API**
   - Accepts image uploads via an API endpoint.
   - Returns the detected license plate text.

---

---

## **🔹 Future Improvements**  
✅ Improve detection accuracy with deep learning-based YOLOv8.  
✅ Add support for video-based license plate recognition.  
✅ Deploy as a web application using Flask and React.  

---

## **🔹 Contributors**  
👤 Richa Gupta
📧 LinkedIn: [Link](https://www.linkedin.com/in/richa-gupta-2ba527247/)

---
