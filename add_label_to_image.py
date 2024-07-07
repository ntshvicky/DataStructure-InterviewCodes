from PIL import Image, ImageDraw, ImageFont

def add_label_to_image(image_path, rectangle_location, label_text, save_path):
    """
    Draws a rectangle and adds a label to an image.

    :param image_path: Path to the original image.
    :param rectangle_location: A tuple (x1, y1, x2, y2) specifying the rectangle's location.
    :param label_text: Text to be added as a label.
    :param label_position: A tuple (x, y) specifying the position of the label.
    :param save_path: Path where the modified image will be saved.
    :return: Image object with the rectangle and label added.
    """
    # Load the image
    image = Image.open(image_path)

    # Draw a rectangle and add a label
    draw = ImageDraw.Draw(image)

    # Draw the rectangle
    draw.rectangle(rectangle_location, outline="red", width=3)

    # Add the label
    try:
        # Use a TrueType font if available
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        # Default font if TrueType is not available
        font = ImageFont.load_default()

    label_position = (rectangle_location[0], rectangle_location[1]-15) # Position where the label text will start


    draw.text(label_position, label_text, fill="blue", font=font)

    # Save the modified image
    image.save(save_path)

    return image

# Example usage of the function:
add_label_to_image("1.png", (50, 50, 150, 150), "Label Name", "1_out.jpg")
