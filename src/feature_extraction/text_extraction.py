from ultralytics import YOLO
import pytesseract
from PIL import Image, UnidentifiedImageError
import os
import logging

def extract_text_with_positions(image_path):
    """
    Extracts text from an image and returns a dictionary mapping the text to its position (bounding box).

    Args:
        image_path: The path to the image file.

    Returns:
        A dictionary where keys are text strings and values are lists of bounding box coordinates
        in the format [x1, y1, x2, y2] (normalized to image width and height).

    Raises:
        FileNotFoundError: If the image file does not exist.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    try:
        # Load image
        img = Image.open(image_path)
    except UnidentifiedImageError:
        logging.error(f"Failed to open image: {image_path}. The file may not be an image or is corrupted.")
        return {}

    img_width, img_height = img.size

    try:
        # Text Detection and OCR (Optical Character Recognition)
        model = YOLO('yolov8n.pt')
    except Exception as e:
        logging.error(f"Failed to load YOLO model: {e}")
        return {}

    text_positions = {}
    try:
        results_yolo = model(image_path)
    except Exception as e:
        logging.error(f"Failed during text detection: {e}")
        return {}

    for result in results_yolo:
        try:
            if result.boxes.cls[0] == 3:  # Filter for 'text' class in YOLOv8 (adjust if needed)
                x1, y1, x2, y2 = result.boxes.xyxy[0]  # Extract coordinates
                cropped_image = img.crop((x1, y1, x2, y2))
                text = pytesseract.image_to_string(cropped_image)  # Perform OCR on cropped region
                if text:
                    normalized_coords = [x1 / img_width, y1 / img_height, x2 / img_width, y2 / img_height]
                    text_positions[text.strip()] = normalized_coords  # Add to dictionary
        except Exception as e:
            logging.warning(f"Failed during OCR or processing a detected text region: {e}")
            continue

    return text_positions
