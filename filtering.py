import os

# Define the directories
mask_dir = r"D:\UsingSpace\HCMUTE\Pratical Machine Learning and Artificial Intelligence\patchcore-inspection-main\patchcore-inspection-main\my_dataset\coffee\ground_truth\colored"
image_dir = r"D:\UsingSpace\HCMUTE\Pratical Machine Learning and Artificial Intelligence\patchcore-inspection-main\patchcore-inspection-main\my_dataset\coffee\test\colored"

# Get lists of all masks and images
masks = {os.path.splitext(f)[0]: f for f in os.listdir(mask_dir) if f.endswith('.png')}
images = {os.path.splitext(f)[0]: f for f in os.listdir(image_dir) if f.endswith('.jpg')}

# Find unmatched masks
for mask_name in list(masks.keys()):
    if mask_name not in images:
        print(f"Removing unmatched mask: {masks[mask_name]}")
        os.remove(os.path.join(mask_dir, masks[mask_name]))

# Find unmatched images
for image_name in list(images.keys()):
    if image_name not in masks:
        print(f"Removing unmatched image: {images[image_name]}")
        os.remove(os.path.join(image_dir, images[image_name]))

print("Cleanup complete.")