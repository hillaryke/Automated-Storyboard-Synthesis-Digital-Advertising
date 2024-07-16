from typing import Final

class Settings:
    ASSISTANT_GENERATOR: Final = 0
    
    IMAGE_COMPOSITION_AGENT_MESSAGE = """
        Compose an AD Frame with the dimensions 600x500 for StoryBoard
        Use the following assets:
        * Header image: header.jpg
        - Should be placed at the top-left corner
        * Instruction image: engagement_instruction_1.png
          - Should be placed at (40, 100)
          - Transparent
        * Thumbnail image: thumbnail.jpg
        - Should be placed at (0, 200)

        The output path is the data folder can be derived from assets path with the name composed_image_frame.jpg

        Return 'TERMINATE' when the task is done.
    """
    
    CONFIG_LIST = [
      {
          "model": "gpt-4o",  # Specifies the model version to be used
      },
    ]
    
    LLM_CONFIG_ASSISTANT = {
        "model": "gpt-4o", # Updated to the latest model version
        "temperature": ASSISTANT_GENERATOR,  # Keeps the creativity level
        "config_list": CONFIG_LIST,  # References the LLM configuration defined above
        "functions": [
            {
                "name": "compose_ad_frame",
                "description": "Composes an advertisement frame using multiple image elements.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "frame_width": {
                            "type": "integer",
                            "description": "Width of the desired frame."
                        },
                        "frame_height": {
                            "type": "integer",
                            "description": "Height of the desired frame."
                        },
                        "elements": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "image_path": {
                                        "type": "string",
                                        "description": "Path to the image file."
                                    },
                                    "position": {
                                        "type": "array",
                                        "items": {
                                            "type": "integer"
                                        },
                                        "minItems": 2,
                                        "maxItems": 2,
                                        "description": "(x, y) coordinates of the top-left corner."
                                    },
                                    "size": {
                                        "type": "array",
                                        "items": {
                                            "type": "integer"
                                        },
                                        "minItems": 2,
                                        "maxItems": 2,
                                        "description": "(width, height) to resize to (maintaining aspect ratio), optional."
                                    },
                                    "has_background": {
                                        "type": "boolean",
                                        "description": "Whether the image has a background (True) or is transparent (False), optional."
                                    }
                                },
                                "required": ["image_path", "position"]
                            },
                            "description": "List of dictionaries, each containing details about the image to be composed."
                        },
                        "output_path": {
                            "type": "string",
                            "description": "Path to save the composed ad frame, optional."
                        },
                    },
                    "required": ["frame_width", "frame_height", "elements"]
                }
            }
        ]
    }