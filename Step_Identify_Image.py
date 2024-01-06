import cv2
from PIL import Image
import numpy as np
import os
import pdb

def find_center_of_contour(contour):
    """Find the center of a given contour."""
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    return cX, cY

def center_and_crop_image(direct_image_path):
    # Read the image
    img = cv2.imread(direct_image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        raise Exception("No contours found in the image")

    # Assuming the largest contour is the item
    largest_contour = max(contours, key=cv2.contourArea)
    item_center_x, item_center_y = find_center_of_contour(largest_contour)

    # Image dimensions and center
    height, width = img.shape[:2]
    center_x, center_y = width // 2, height // 2

    # Calculate the offset
    offset_x, offset_y = center_x - item_center_x, center_y - item_center_y

    # Create a new blank image and place the original image shifted by the offset
    new_img = np.zeros_like(img)
    translation_matrix = np.float32([[1, 0, offset_x], [0, 1, offset_y]])
    shifted_img = cv2.warpAffine(img, translation_matrix, (width, height), new_img, borderMode=cv2.BORDER_CONSTANT)

    # Convert to PIL Image for easier cropping
    pil_img = Image.fromarray(cv2.cvtColor(shifted_img, cv2.COLOR_BGR2RGB))
    return pil_img

# Define the directory containing the input images
input_directory = "/Users/isabellaarroyo/Desktop/Image_Resizing_Project/Final_Wines"

# Define the directory to save the centered images
output_directory = "/Users/isabellaarroyo/Desktop/Image_Resizing_Project/Test2ResizedWine"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List of input image file names
input_image_files = [
    "DSC_0002.JPG",
    "DSC_0003.JPG",
    "DSC_0004.JPG",
    "DSC_0005.JPG",
    "DSC_0006.JPG",
    "DSC_0007.JPG",
    "DSC_0008.JPG",
    ]


# Loop through the input image files and resize each one
for input_image_file in input_image_files:
    # Open the input image file
    # pdb.set_trace()
    input_image_path = os.path.join(input_directory, input_image_file)
    print("Image path: " + input_image_path)

    # Close the original and resized images
    image = Image.open(input_image_path)

    # Use the function on an image
    centered_image = center_and_crop_image(input_image_path)
    centered_image.show()

    # Define the output file path
    output_image_path = os.path.join(output_directory, input_image_file)

    # Save the resized image to the output file path
    centered_image.save(output_image_path)

    
    image.close()
    

print("Centering and Resizing complete.")


# Use the function on an image
# centered_image = center_and_crop_image("Final_Wines/DSC_0003.JPG")
# centered_image.show()
