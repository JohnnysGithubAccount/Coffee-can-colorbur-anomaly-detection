import os
from PIL import Image

# Define the path to the directory containing the images
input_dir = r"D:\UsingSpace\HCMUTE\Pratical Machine Learning and Artificial Intelligence\patchcore-inspection-main\patchcore-inspection-main\my_dataset\coffee\ground_truth\colored"

# Iterate through all files in the directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.png'):
        # Construct full file path
        file_path = os.path.join(input_dir, filename)
        try:
            # Open an image file
            with Image.open(file_path) as img:
                # Convert image to grayscale
                img = img.convert("L")

                # Create a binary image
                binary_img = img.point(lambda p: 1 if p > 0 else 0, '1')

                # Save the binary image, overwriting the original or saving as a new file
                binary_img.save(file_path)
                print(f"Converted to binary: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

print("Conversion to binary complete.")