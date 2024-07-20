from PIL import Image, UnidentifiedImageError

def has_transparency(image_path):
    """
    Checks for transparency in an image using Pillow with advanced error handling.

    Args:
        image_path (str): Path to the image file.

    Returns:
        bool: True if the image has transparency, False otherwise.
    """
    try:
        img = Image.open(image_path)
        img_mode = img.mode

        if img_mode in ('RGBA', 'LA'):
            return True
        elif img_info := img.info.get('transparency', None):
            return True  # Transparency defined in info dictionary

        return False  # No transparency detected

    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return False
    except PermissionError:
        print(f"Error: Permission denied to access {image_path}.")
        return False
    except UnidentifiedImageError:
        print(f"Error: The file {image_path} is not a recognized image format.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

### Example usage
# assets_path = "path/to/assets"  # Define the correct path to your assets
# image_path = f"{assets_path}/thumbnail.jpg"
# has_transparent_background = has_transparency(image_path)
# print(has_transparent_background)