import os
from PIL import Image, ImageDraw, ImageFont
import cv2

def add_text_to_images(input_folder, output_folder, font_path):
    """
    Adds text (image filename) to each image in the input folder and saves the processed images in the output folder.
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # List all TIFF files in the input folder
    images = [img for img in os.listdir(input_folder) if img.endswith('.tiff')]

    # Load a font
    font = ImageFont.truetype(font_path, 36)  # Adjust the size as needed

    for image_name in images:
        # Open an image file
        with Image.open(os.path.join(input_folder, image_name)) as img:
            draw = ImageDraw.Draw(img)
            # Define text position (bottom left corner)
            text_position = (10, img.height - 40)  # Adjust position as needed
            # Draw the image name onto the image
            draw.text(text_position, image_name, font=font, fill="white")

            # Save the image as JPEG in the output folder
            output_image_path = os.path.join(output_folder, image_name.replace('.tiff', '.jpeg'))
            img.save(output_image_path, 'JPEG')

def create_video_from_images(image_folder, video_path, fps):
    """
    Creates a video from images in the specified folder.
    """
    # Ensure the directory for the video path exists
    video_dir = os.path.dirname(video_path)
    if not os.path.exists(video_dir):
        os.makedirs(video_dir)
    
    # List all JPEG files in the image folder
    image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith('.jpeg')]
    image_files.sort()  # Ensure the images are in the correct order

    if not image_files:
        print("No images to process for the video.")
        return

    # Get the size of the first image
    frame = cv2.imread(image_files[0])
    height, width, layers = frame.shape

    # Define the video codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec if needed
    video = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

    for image_file in image_files:
        img = cv2.imread(image_file)
        video.write(img)

    # Release the video writer object
    video.release()

# Define your paths and parameters
input_folder = 'path/to/your/input/folder'
output_folder = 'path/to/your/output/folder'
font_path = 'path/to/your/font.ttf'  # Ensure you have a valid font file path
video_path = 'path/to/your/output/video.mp4'
fps = 30  # Frames per second

# Uncomment the function call you need to use

# Add text to images
# add_text_to_images(input_folder, output_folder, font_path)

# Create video from images
# create_video_from_images(output_folder, video_path, fps)
