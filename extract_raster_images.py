import xml.etree.ElementTree as ET
import base64
import os

def extract_images_from_svg(svg_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    tree = ET.parse(svg_file)
    root = tree.getroot()
    
    # Find all <image> tags
    for image in root.findall('.//{http://www.w3.org/2000/svg}image'):
        image_data = image.get('{http://www.w3.org/1999/xlink}href')
        if image_data.startswith('data:image/png;base64,'):
            image_data = image_data[len('data:image/png;base64,'):]
            image_bytes = base64.b64decode(image_data)
            
            image_filename = os.path.join(output_dir, f"extracted_image_{image.get('id', 'unnamed')}.png")
            with open(image_filename, 'wb') as f:
                f.write(image_bytes)
                
    print(f"Extracted images are saved in '{output_dir}'.")

# Example usage
extract_images_from_svg('handwritten_sample.svg', 'extracted_images')
