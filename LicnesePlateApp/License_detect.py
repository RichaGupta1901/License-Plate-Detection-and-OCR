import cv2
import pytesseract
import os
import easyocr

# Load the pre-trained Haar cascade
plate_cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
reader = easyocr.Reader(['en'])  # Load English OCR model

# Set Tesseract path (only for Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\richa\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def detect_license_plate_ocr(image_path):
    image = cv2.imread(image_path)

    if image is None:  # Check if image is loaded properly
        raise ValueError(f"Error: Unable to load image '{image_path}'")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect license plates
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    plate_texts = []

    for (x, y, w, h) in plates:
        # Draw rectangle around detected plate
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(image, "Plate", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Crop the detected plate
        plate_roi = gray[y:y + h, x:x + w]

        # OCR using EasyOCR (preferred)
        plate_number_easy = reader.readtext(plate_roi, detail=0)
        plate_number_easy = ' '.join(plate_number_easy)  # Convert list to string

        # OCR using Tesseract (backup)
        plate_number_tess = pytesseract.image_to_string(
            plate_roi, config="--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        ).strip()

        """
        # If you want to check which OCR engine is used
        if plate_number_easy and plate_number_tess:
            best_ocr = "EasyOCR" if len(plate_number_easy) > len(plate_number_tess) else "Tesseract"
            best_text = plate_number_easy if best_ocr == "EasyOCR" else plate_number_tess
        elif plate_number_easy:
            best_ocr = "EasyOCR"
            best_text = plate_number_easy
        elif plate_number_tess:
            best_ocr = "Tesseract"
            best_text = plate_number_tess
        else:
            best_ocr = "None"
            best_text = "No text detected"

        # Store results with OCR source
        plate_results.append({"text": best_text, "detected_by": best_ocr})

        # return plate_results instead of plate_texts at the end of the function
        """

        # Choose the best result
        final_plate_text = plate_number_easy if plate_number_easy else plate_number_tess

        if final_plate_text:
            plate_texts.append(final_plate_text)

    # Save output image
    output_path = os.path.join("uploads", "output_" + os.path.basename(image_path))
    cv2.imwrite(output_path, image)

    return output_path, plate_texts
