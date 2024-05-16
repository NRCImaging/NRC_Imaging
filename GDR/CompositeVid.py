import cv2
import numpy as np
import os

# Function to load and sum every 10 images
def sum_images(start_index, end_index, sum_path):
    # Load the images
    images = [cv2.imread('W:\\data\\EbrahimGDR\\2.Output\\Python\\Staking\\images' + str(i).zfill(4) + '.tiff') for i in range(start_index, end_index)]
    # Convert images to float32 for accurate calculations
    images_float = [np.float32(img) for img in images]
    # Stack images by taking the average pixel value
    composite_image = np.sum(images_float, axis=0).astype(np.uint8)
    # Save the composite image
    cv2.imwrite(os.path.join(sum_path, 'composite_image{}.jpg'.format(start_index)), composite_image)

# Directory to save the composite images
sum_path = 'W:\\data\\composite_images'

# Create the directory if it doesn't exist
if not os.path.exists(sum_path):
    os.makedirs(sum_path)

# Loop through all images in increments of 10
for i in range(1, 6001, 10):
    sum_images(i, i + 10, sum_path)

# Create a video from the composite images
image_folder = sum_path
output_directory = 'W:\\data\\video_output'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

video_name = os.path.join(output_directory, 'output_video.avi')

# Get a sorted list of all composite images
images = sorted([img for img in os.listdir(image_folder) if img.endswith(".jpg")])

# Read the first image to get the dimensions
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID') # You can try other codecs like 'MJPG' or 'MP4V'
fps = 15  # Set the desired frame rate (frames per second)
video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

# Write each image to the video
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

# Release the video writer
video.release()
cv2.destroyAllWindows()
