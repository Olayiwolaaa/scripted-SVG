import random
from PIL import Image
import svgwrite, os

def get_random_variation(character):
    char_dir = os.path.join('labeled_characters', character)
    variations = os.listdir(char_dir)
    return os.path.join(char_dir, random.choice(variations))

def generate_handwritten_svg(input_text, output_svg_file):
    dwg = svgwrite.Drawing(output_svg_file, profile='tiny')
    
    x_offset = 0
    for char in input_text:
        if char.strip() == '':  # Ignore spaces
            x_offset += 20
            continue
        
        char_image_path = get_random_variation(char.upper())  # Assuming uppercase labels
        char_image = Image.open(char_image_path)
        
        # Slight randomness in position and scale
        random_shift_x = random.randint(-5, 5)
        random_shift_y = random.randint(-5, 5)
        x_offset += char_image.width + random.randint(0, 10)
        
        dwg.add(dwg.image(char_image_path, insert=(x_offset + random_shift_x, random_shift_y), size=(char_image.width, char_image.height)))

    dwg.save()

# Example Usage
generate_handwritten_svg('A1B1', 'output_handwritten.svg')
