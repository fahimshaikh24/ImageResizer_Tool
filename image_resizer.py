#Image Resizer Tool
#Author : Fahim Shaikj
from PIL import Image
import os

# Input and output folder paths
input_folder = "images_input"     
output_folder = "images_output" 

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Set the target size (width, height)
new_size = (400, 400)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize the image
        img_resized = img.resize(new_size)

        # Save the resized image in the output folder
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
        img_resized.save(output_path, "JPEG")

        print(f"✅ Resized and saved: {output_path}")

print("\n All images resized successfully!")
