import cairosvg
from PIL import Image
import cv2
import os

# Convert SVG to PNG for processing
def convert_svg_to_png(svg_file, output_file):
    cairosvg.svg2png(url=svg_file, write_to=output_file)

# Segment characters using OpenCV
def segment_characters(image_file, output_dir):
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    # Threshold the image to binary (black & white)
    _, binary_image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours (assumed to be the characters)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, contour in enumerate(contours):
        # Bounding box for each character
        x, y, w, h = cv2.boundingRect(contour)
        char_image = image[y:y+h, x:x+w]
        cv2.imwrite(f"{output_dir}/char_{i}.png", char_image)

# Example Usage
convert_svg_to_png('handwritten_sample.svg', 'output.png')
segment_characters('output.png', 'character_output')
