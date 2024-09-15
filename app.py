import pytesseract
from PIL import Image
import cv2

# Load your scanned document (as an image)
image_path = 'handwritten_sample.jpg'
img = cv2.imread(image_path)

# Convert the image to grayscale for better OCR results
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Use pytesseract to perform OCR and get bounding boxes for each character
custom_config = r'--oem 3 --psm 6'  # OEM 3: Default, PSM 6: Assume a single uniform block of text
data = pytesseract.image_to_boxes(gray, config=custom_config)

# Parse the output to get each character and its bounding box
for char in data.splitlines():
    char_data = char.split(' ')
    character = char_data[0]  # Character itself
    x1, y1, x2, y2 = map(int, char_data[1:5])  # Bounding box coordinates
    print(f"Character: {character}, Box: {x1}, {y1}, {x2}, {y2}")

    # Crop each character from the image using its bounding box
    char_img = img[y1:y2, x1:x2]
    cv2.imwrite(f'output/{character}_{x1}_{y1}.png', char_img)  # Save each character
