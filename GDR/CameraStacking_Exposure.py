import cv2
import time
from vimba import *

# Set exposure time in microseconds
exposure_time = 5000  # Example: 5000 microseconds

with Vimba.get_instance() as vimba:
    cams = vimba.get_all_cameras()

    with cams[0] as cam:
        # Set exposure time
        cam.ExposureTimeAbs.set(exposure_time)

        i = 1
        while i < 2000:
            for _ in range(10):  # Capture 10 images
                print("image" + str(i).zfill(4))
                frame = cam.get_frame()
                frame.convert_pixel_format(PixelFormat.Bgr8)
                cv2.imwrite(('W:\\data\\2024\\images' + str(i).zfill(4) + '.tiff'), frame.as_opencv_image(), params=(cv2.IMWRITE_TIFF_COMPRESSION, 1))
                time.sleep(3)
                i += 1
            print("Waiting for 300 seconds...")
            time.sleep(300)  # Wait for 300 seconds before capturing the next set of 10 images
