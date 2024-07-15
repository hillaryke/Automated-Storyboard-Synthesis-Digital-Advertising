import unittest
import os
from PIL import Image

os.chdir("../")
from src.image_composition import compose_ad_frame
from tempfile import TemporaryDirectory

class TestComposeAdFrame(unittest.TestCase):
	def test_compose_ad_frame(self):
		with TemporaryDirectory() as tmpdir:
			# Setup test images
			base_image_path = os.path.join(tmpdir, 'base.jpg')
			overlay_image_path = os.path.join(tmpdir, 'overlay.png')
			output_image_path = os.path.join(tmpdir, 'composed.jpg')

			# Create a base image
			base_image = Image.new('RGB', (600, 400), color = 'blue')
			base_image.save(base_image_path)

			# Create an overlay image with transparency
			overlay_image = Image.new('RGBA', (200, 200), color = (255,0,0,128))  # Red, half-transparent
			overlay_image.save(overlay_image_path)

			# Define elements to compose
			elements = [
				{'image_path': base_image_path, 'position': (0, 0), 'has_background': True},
				{'image_path': overlay_image_path, 'position': (200, 100), 'has_background': False},
			]

			# Invoke compose_ad_frame
			composed_image = compose_ad_frame(600, 400, elements, output_image_path)

			# Asserts
			self.assertTrue(os.path.exists(output_image_path), "Output image file should exist.")
			self.assertEqual(composed_image.size, (600, 400), "Composed image should have the expected dimensions.")

			# Optionally, verify the content of the composed image
			# This could involve checking pixel values at certain positions, etc.

if __name__ == '__main__':
	unittest.main()