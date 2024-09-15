import os
import extract_raster_images
import segment_and_label
import generate_svg

def main():
    # Step 1: Extract Raster Images from SVG
    svg_file = 'handwritten_sample.svg'
    extracted_images_dir = 'extracted_images'
    
    print("Extracting raster images from SVG...")
    extract_raster_images.extract_images_from_svg(svg_file, extracted_images_dir)

    # Step 2: Segment and Label Characters
    character_output_dir = 'character_output'
    
    print("Segmenting characters...")
    for img_file in os.listdir(extracted_images_dir):
        img_path = os.path.join(extracted_images_dir, img_file)
        segment_and_label.segment_characters(img_path, character_output_dir)
    
    # Ensure the directory exists before labeling
    if not os.path.exists(character_output_dir):
        print(f"Error: '{character_output_dir}' does not exist.")
        return
    else:
        print(f"'{character_output_dir}' directory verified.")
    
    print("Labeling characters...")
    segment_and_label.label_characters(character_output_dir)

    # Step 3: Generate Handwritten SVG based on Input
    input_text = input("Enter the text to generate handwritten SVG: ")
    output_svg_file = 'output_handwritten.svg'
    width_mm = float(input("Enter the width of the SVG document in millimeters: "))
    height_mm = float(input("Enter the height of the SVG document in millimeters: "))
    
    print(f"Generating handwritten SVG for input text: {input_text}")
    generate_svg.generate_handwritten_svg(input_text, output_svg_file, width_mm, height_mm)
    
    print(f"Handwritten SVG has been generated: {output_svg_file}")

if __name__ == "__main__":
    main()
