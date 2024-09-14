# HandwriteSVG

**HandwriteSVG** is an SVG generator that creates custom handwritten text using pre-labeled character paths. The application introduces randomness in character selection and placement to simulate natural handwriting, ensuring each output looks slightly different even for the same input.

## Features

- Label and store individual characters (letters, numbers, etc.) from a handwritten sample.
- Support multiple variations for each character.
- Dynamically generate SVG files from text input.
- Add randomness to character selection and positioning to create natural handwriting effects.
- Customize document size using millimeters as a unit of measurement.

## How It Works

1. **Label Handwritten Characters**:
    - Store each character (A-Z, 0-9) and its variations as separate paths.
  
2. **Text Input**:
    - Input a simple sentence or a string of text.
  
3. **Generate SVG**:
    - The system retrieves the corresponding characters, picks random variations, and applies slight randomness to their placement.
  
4. **Output**:
    - An SVG file is generated with handwritten characters formatted to the specified document size.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/HandwriteSVG.git
    cd HandwriteSVG
    ```

2. Install necessary dependencies (e.g., for Python, Node.js, or other technologies used in your project):

    ```bash
    # Example for a Python project
    pip install -r requirements.txt
    ```

3. If needed, set up any environment variables or configuration files.

## Usage

1. Label your characters:
    - Prepare an SVG file containing handwritten characters.
    - Store paths for each character in the `data/` directory (or wherever you've set up your labeled characters).

2. Input a sentence or string:
    
    ```bash
    python generate_svg.py "Your text input here"
    ```

3. Customize the document size:

    ```bash
    python generate_svg.py "Your text input" --width 210mm --height 297mm
    ```

4. Check the generated SVG file in the `output/` directory.

## Example

```bash
python generate_svg.py "Hello 123"
