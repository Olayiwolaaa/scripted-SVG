import cairosvg
from PIL import Image
import cv2
import os

def convert_svg_to_png(svg_file, output_file):
    cairosvg.svg2png(url=svg_file, write_to=output_file)

def segment_characters(image_file, output_dir):
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    _, binary_image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
    
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        char_image = image[y:y+h, x:x+w]
        cv2.imwrite(f"{output_dir}/char_{i}.png", char_image)

def extract_and_label_characters(image_file, output_dir):
    convert_svg_to_png(image_file, 'temp_image.png')
    segment_characters('temp_image.png', output_dir)
    os.remove('temp_image.png')
