from PIL import Image

def get_image_dimensions(image_path):
    """Gets the dimensions (width, height) of an image using Pillow.

    Args:
        image_path (str): The path to the image file.

    Returns:
        tuple: A tuple containing the width and height of the image (width, height), or None if there's an error.
    """
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except (FileNotFoundError, PIL.UnidentifiedImageError) as e:
        print(f"Error: Unable to get dimensions for '{image_path}': {e}")
        return None

# Example usage
if __name__ == "__main__":
    image_path = 'data/Assets/3c99774ddf5babcf91ae21f76e9f4508/_preview.png'
    dimensions = get_image_dimensions(image_path)
    if dimensions:
        width, height = dimensions
        print(f"Dimensions of '{image_path}': {width} x {height}")