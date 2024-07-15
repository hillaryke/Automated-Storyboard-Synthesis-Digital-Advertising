from PIL import Image

from PIL import Image

def load_and_prepare_image(image_path, target_size=None, has_background=True):
    """
    Loads an image, resizes it if a target size is specified, and prepares it for composition.

    Args:
        image_path (str): Path to the image file.
        target_size (tuple, optional): Desired (width, height) to resize the image.
        has_background (bool): Indicates if the image has a background.

    Returns:
        PIL.Image: The prepared image.
    """
    img = Image.open(image_path).convert('RGBA')
    if target_size:
        img = img.resize(target_size, Image.Resampling.LANCZOS)
    return img

def paste_image(base_image, img, position, has_background=True):
    """
    Pastes an image onto the base image, considering transparency.

    Args:
        base_image (PIL.Image): The base image.
        img (PIL.Image): The image to paste.
        position (tuple): (x, y) position to paste the image.
        has_background (bool): Indicates if the image has a background.
    """
    if has_background:
        base_image.paste(img, position, img.split()[3] if img.mode == 'RGBA' else None)
    else:
        base_image.alpha_composite(img, position)

from PIL import Image

def compose_ad_frame(frame_width, frame_height, elements):
    """
    Composes an advertisement frame using multiple image elements.

    Args:
        frame_width (int): Width of the desired frame.
        frame_height (int): Height of the desired frame.
        elements (list): List of dictionaries, each containing:
            - image_path (str): Path to the image file.
            - position (tuple): (x, y) coordinates of the top-left corner.
            - size (tuple, optional): (width, height) to resize to (maintaining aspect ratio).
            - has_background (bool): Whether the image has a background (True) or is transparent (False).

    Returns:
        PIL.Image: The composed ad frame.
    """

    # Create a new blank RGBA image
    composed_frame = Image.new('RGBA', (frame_width, frame_height))

    for element in elements:
        # Load and convert image to RGBA
        img = Image.open(element['image_path']).convert('RGBA')

        # Resize if size is provided
        if 'size' in element:
            width, height = img.size
            aspect_ratio = width / height
            new_width, new_height = element['size']
            if new_width / new_height > aspect_ratio:
                new_width = int(new_height * aspect_ratio)
            else:
                new_height = int(new_width / aspect_ratio)
            img = img.resize((new_width, new_height))

        # Paste the image onto the frame
        if element.get('has_background', True):  # Default to True if not specified
            composed_frame.paste(img, element['position'])
        else:
            composed_frame.alpha_composite(img, element['position'])

    # Convert to RGB and return
    return composed_frame.convert('RGB')

## Example usage
## assets_path = '/path/to/assets'
# elements = [
#     {'image_path': f'{assets_path}/header.jpg', 'position': (0, 0), 'has_background': True},
#     {'image_path': f'{assets_path}/engagement_instruction_1.png', 'position': (40, 100), 'has_background': False},
#     {'image_path': f'{assets_path}/thumbnail.jpg', 'position': (0, 200), 'size': get_image_dimensions(f'{assets_path}/thumbnail.jpg'), 'has_background': True}
# ]

# composed_frame = compose_ad_frame(600, 500, elements)
# composed_frame.show()  # Or save using composed_frame.save('composed_frame.jpg')
