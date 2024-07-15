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
