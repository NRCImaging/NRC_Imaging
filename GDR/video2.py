import cv2
import os

def make_video(image_folder, video_name):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width,height))

    for image in images:
        img = cv2.imread(os.path.join(image_folder, image))
        cv2.putText(img, image, (width - 300, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        video.write(img)

    cv2.destroyAllWindows()
    video.release()

# Specify the folder containing the images and the name of the output video
image_folder = 'path_to_your_image_folder'
video_name = 'output_video.avi'

make_video(image_folder, video_name)
