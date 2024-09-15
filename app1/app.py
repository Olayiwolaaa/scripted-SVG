import parse_and_label
import store_and_label
import generate_svg

def main():
    # Step 1: Extract and Label Characters from the SVG
    svg_file = 'handwritten_sample.svg'
    character_output_dir = 'character_output'
    
    print("Extracting and labeling characters from SVG...")
    parse_and_label.extract_and_label_characters(svg_file, character_output_dir)

    # Step 2: Store and Label Characters
    print("Labeling characters...")
    store_and_label.label_characters(character_output_dir)

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
