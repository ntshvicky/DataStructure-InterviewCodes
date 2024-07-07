from PIL import Image

# Path to your original image
original_image_path = '1_out.jpg'

# Load the original image
original_image = Image.open(original_image_path)

# Resize the image to 240x240 pixels using the LANCZOS filter
resized_image = original_image.resize((800, 800), Image.LANCZOS)

# Path for saving the resized image
resized_image_path = 'resized_ladybug_panoramic_000003.jpg'

# Save the resized image
resized_image.save(resized_image_path)

print(f"Image resized and saved as {resized_image_path}")
