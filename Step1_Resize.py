from PIL import Image
import os

# Define the directory containing the input images
input_directory = "/Users/isabellaarroyo/Desktop/Sample_Earring/Raw"

# Define the directory to save the resized images
output_directory = "/Users/isabellaarroyo/Desktop/Sample_Earring/Resized_512_x_512"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Define the new size (width, height) you want for the images
new_size = (512, 512)  # Change these values to your desired dimensions

# List of input image file names
input_image_files = [
    "IMG_6022.jpeg",
    "IMG_6023.jpeg",
    "IMG_6024.jpeg",
    "IMG_6025.jpeg",
    "IMG_6026.jpeg",
    "IMG_6027.jpeg",
    "IMG_6028.jpeg",
    "IMG_6029.jpeg",
    "IMG_6030.jpeg",
    "IMG_6031.jpeg",
    "IMG_6032.jpeg",
    "IMG_6033.jpeg",
    "IMG_6034.jpeg",
    "IMG_6036.jpeg",
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
