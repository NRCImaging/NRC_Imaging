import os
from PIL import Image, ImageDraw, ImageFont
import cv2
####
#
####

# Define your paths and parameters
input_folder = 'path/to/your/input/folder'
output_folder = 'path/to/your/output/folder'
font_path = 'path/to/your/font.ttf'  # Ensure you have a valid font file path
video_path = 'path/to/your/output/video.mp4'
fps = 30  # Frames per second



def process_images(input_folder, output_folder, font_path, video_path, fps):
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
    
    # Create a video from the images
    image_files = [os.path.join(output_folder, img) for img in os.listdir(output_folder) if img.endswith('.jpeg')]
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



# Process the images and create the video
process_images(input_folder, output_folder, font_path, video_path, fps)
