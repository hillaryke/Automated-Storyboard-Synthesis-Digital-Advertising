import os
import pytesseract
from pytesseract import Output
from PIL import Image, UnidentifiedImageError
import logging

def extract_text_with_positions(image_path):
    """
    Extracts text and their bounding boxes from an image.

    Args:
        image_path (str): The path to the image file.

    Returns:
        dict: A dictionary where keys are the extracted text strings and values are tuples
              representing the bounding box of the text in the format (left, top, right, bottom).

    Raises:
        FileNotFoundError: If the image file does not exist.
        Exception: For errors related to image loading and OCR processing.
        
    Example Usage:
        header_image_path = "/home/hillary_kipkemoi/Automated-Storyboard-Synthesis-Digital-Advertising/data/Assets/0a22f881b77f00220f2034c21a18b854/header.jpg"
        result = extract_text_with_positions(header_image_path)
    """
    # Check if the image file exists
    try:
        # Load the image using Pillow
        img = Image.open(image_path)
    except FileNotFoundError as e:
        logging.error(f"Image file not found: {e}")
        raise
    except UnidentifiedImageError as e:
        logging.error(f"Failed to open image: {e}. The file may not be an image or is corrupted.")
        raise Exception("Failed to load image with PIL.") from e

    try:
        # Use pytesseract to get the bounding boxes
        data = pytesseract.image_to_data(img, output_type=Output.DICT)
    except Exception as e:
        logging.error(f"Failed during OCR processing: {e}")
        raise Exception("OCR processing failed.") from e

    # Initialize the result dictionary
    text_positions = {}

    # Iterate through the data to extract text and their positions
    n_boxes = len(data['level'])
    for i in range(n_boxes):
        if data['text'][i].strip():  # Check if the text is not empty
            text = data['text'][i]
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            # Store the position as a tuple (left, top, right, bottom)
            text_positions[text] = (x, y, x + w, y + h)

    return text_positions
