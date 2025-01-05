import os
from PIL import Image

# Define the path to the directory containing subdirectories of images
base_dir = r"D:\UsingSpace\HCMUTE\Pratical Machine Learning and Artificial Intelligence\patchcore-inspection-main\patchcore-inspection-main\my_dataset\coffee"

# Iterate through all subdirectories and files
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Include common image formats
            # Construct full file path
            file_path = os.path.join(root, file)
            try:
                # Open an image file
                with Image.open(file_path) as img:
                    # Resize image
                    img = img.resize((900, 900), Image.LANCZOS)
                    # Save the resized image, overwriting the original
                    img.save(file_path)
                    print(f"Resized and saved: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

print("Resizing complete.")