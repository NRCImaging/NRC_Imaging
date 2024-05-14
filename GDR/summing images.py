import cv2 
import numpy as np

# Function to load and sum every 10 images
def sum_images(start_index, end_index):
    # Load the images
    images = [cv2.imread('W:\\data\\EbrahimGDR\\2.Output\\Python\\Staking\\images' + str(i).zfill(4) + '.tiff') for i in range(start_index, end_index)]
    # Convert images to float32 for accurate calculations
    images_float = [np.float32(img) for img in images]
    # Stack images by taking the average pixel value
    composite_image = np.sum(images_float, axis=0).astype(np.uint8)
    # Save the composite image
    cv2.imwrite('composite_image{}.jpg'.format(start_index), composite_image)

# Loop through all images in increments of 10
for i in range(1, 6001, 10):
    sum_images(i, i+10)
