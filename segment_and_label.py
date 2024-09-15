import cv2
import os
from PIL import Image

def segment_characters(image_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
        
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error loading image file: {image_file}")
        return
    
    _, binary_image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        print("No contours found.")
    
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        char_image = image[y:y+h, x:x+w]
        char_image_path = f"{output_dir}/char_{i}.png"
        cv2.imwrite(char_image_path, char_image)
        print(f"Saved segmented character: {char_image_path}")


def label_characters(image_dir):
    if not os.path.exists(image_dir):
        print(f"Error: '{image_dir}' does not exist.")
        return

    image_files = os.listdir(image_dir)
    if not image_files:
        print(f"No images found in '{image_dir}'.")
        return

    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        image = Image.open(image_path)
        image.show()
        
        label = input("Enter the label for this character (e.g., 'A', 'B', '1'): ").strip()
        variation_dir = os.path.join('labeled_characters', label)
        
        if not os.path.exists(variation_dir):
            os.makedirs(variation_dir)
        
        variation_count = len(os.listdir(variation_dir)) + 1
        image.save(f"{variation_dir}/{label}_variation{variation_count}.png")

        
# Example usage
for img_file in os.listdir('extracted_images'):
    segment_characters(os.path.join('extracted_images', img_file), 'character_output')

label_characters('character_output')
