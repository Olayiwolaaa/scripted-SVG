import random
from PIL import Image
import svgwrite
import os

def get_random_variation(character):
    char_dir = os.path.join('labeled_characters', character)
    if not os.path.exists(char_dir):
        print(f"Directory does not exist: {char_dir}")
        return None
    variations = os.listdir(char_dir)
    if not variations:
        print(f"No variations found for character: {character}")
        return None
    return os.path.join(char_dir, random.choice(variations))

def generate_handwritten_svg(input_text, output_svg_file, width_mm, height_mm):
    dwg = svgwrite.Drawing(output_svg_file, profile='tiny', size=(f'{width_mm}mm', f'{height_mm}mm'))
    
    x_offset = 0
    y_offset = 0
    line_height = 30  # Adjust based on your needs
    
    for char in input_text:
        if char.strip() == '':
            x_offset += 10
            continue
        
        char_image_path = get_random_variation(char.upper())
        if not char_image_path:
            print(f"No variations found for character: {char}")
            continue
        
        char_image = Image.open(char_image_path)
        
        random_shift_x = random.randint(-2, 2)
        random_shift_y = random.randint(-2, 2)
        x_offset += char_image.width + random.randint(0, 5)
        
        temp_image_path = f'temp_{char}.png'
        char_image.save(temp_image_path)
        
        dwg.add(dwg.image(temp_image_path, insert=(x_offset + random_shift_x, y_offset + random_shift_y), size=(char_image.width, char_image.height)))
        
        os.remove(temp_image_path)
        
        if x_offset > 190:  # Arbitrary value, adjust based on width
            x_offset = 0
            y_offset += line_height
    
    dwg.save()
