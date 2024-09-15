import os
from PIL import Image

def label_characters(image_dir):
    for image_file in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_file)
        image = Image.open(image_path)
        image.show()
        
        label = input("Enter the label for this character (e.g., 'A', 'B', '1'): ").strip()
        variation_dir = os.path.join('labeled_characters', label)
        
        if not os.path.exists(variation_dir):
            os.makedirs(variation_dir)
        
        variation_count = len(os.listdir(variation_dir)) + 1
        image.save(f"{variation_dir}/{label}_variation{variation_count}.png")
