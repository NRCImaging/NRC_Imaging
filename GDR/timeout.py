import cv2
import time
from vimba import *

# Set exposure time in microseconds (9 seconds)
exposure_time = 9000000  # 9 seconds in microseconds

with Vimba.get_instance() as vimba:
    cams = vimba.get_all_cameras()

    with cams[0] as cam:
        # Set exposure time
        cam.ExposureTime.set(exposure_time)  # Set the exposure time

        i = 1
        while i < 2000:
            for _ in range(10):  # Capture 10 images
                print("image" + str(i).zfill(4))
                
                # Increase the timeout to accommodate the long exposure time
                frame = cam.get_frame(timeout_ms=12000)  # Set timeout to 12 seconds (12000 milliseconds)

                frame.convert_pixel_format(PixelFormat.Bgr8)
                cv2.imwrite(('W:\\data\\Python\\images' + str(i).zfill(4) + '.tiff'), frame.as_opencv_image(), params=(cv2.IMWRITE_TIFF_COMPRESSION, 1))
                i += 1
            print("Waiting for 300 seconds...")
            time.sleep(300)  # Wait for 300 seconds before capturing the next set of 10 images
