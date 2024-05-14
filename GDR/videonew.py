import cv2
import os

# Directory containing the images
image_folder = 'path/to/your/images'

# Video name
video_name = 'output_video.mp4'

# Sort the images based on their names
images = sorted([img for img in os.listdir(image_folder) if img.endswith(".jpg")])

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # You can change the codec as needed
video = cv2.VideoWriter(video_name, fourcc, 10, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
