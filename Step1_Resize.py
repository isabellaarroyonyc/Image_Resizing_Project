from PIL import Image
import os

# Define the directory containing the input images
input_directory = "/Users/isabellaarroyo/Desktop/Image_Resizing_Project/Final_Wines"

# Define the directory to save the resized images
output_directory = "/Users/isabellaarroyo/Desktop/Sample_Earring/Image_Resizing_Project/Test_Step1_Resize"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Define the new size (width, height) you want for the images
new_size = (512, 512)  # Change these values to your desired dimensions

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
    input_image_path = os.path.join(input_directory, input_image_file)
    image = Image.open(input_image_path)

    # Resize the image
    resized_image = image.resize(new_size)

    # Define the output file path
    output_image_path = os.path.join(output_directory, input_image_file)

    # Save the resized image to the output file path
    resized_image.save(output_image_path)

    # Close the original and resized images
    image.close()
    resized_image.close()

print("Resize complete.")
