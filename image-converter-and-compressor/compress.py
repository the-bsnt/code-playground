"""Compress a JPG/PNG images to a specified quality level and size."""
from PIL import Image


def compress_image(input_image_path, output_image_path, quality):
    with Image.open(input_image_path) as img:
        img.save(output_image_path, "JPEG", quality=quality)


"""
    EDIT FOLLOWING PARAMETERS
    input_image_path: Give Path of image file to compress.
    output_image_path: Give Path where the compressed image [output] will be saved.
    quality: Adjust the quality (1-100), lower means more compression.
    """
input_image_path = "sample.jpg"
output_image_path = "compressed_sample.jpg"
quality = 30   
compress_image(input_image_path, output_image_path, quality)
