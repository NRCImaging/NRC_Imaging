import rawpy
import imageio
from vimba import *

def setup_camera(cam):
    # Set camera settings here (e.g., exposure time)
    pass

def print_preamble():
    # Print any necessary preamble or instructions
    pass

def parse_args():
    # Parse any necessary command-line arguments
    return 'DEV_1AB22C015841'  # Example camera ID, replace with actual ID

def get_camera(cam_id):
    vimba = Vimba.get_instance()
    cams = vimba.get_all_cameras()
    for cam in cams:
        if cam.get_id() == cam_id:
            return cam
    raise RuntimeError(f'Camera with ID {cam_id} not found.')

def save_as_dng(raw_frame, width, height, filename):
    # Create a rawpy object from the raw_frame data
    raw_image = rawpy.imread(raw_frame)

    # Save as DNG using imageio
    imageio.imsave(filename, raw_image.raw_image, format='DNG')

def main():
    print_preamble()
    cam_id = parse_args()

    with Vimba.get_instance() as vimba:
        with get_camera(cam_id) as cam:
            setup_camera(cam)

            # Acquire 10 frames with a custom timeout (default is 2000ms) per frame acquisition
            for i, frame in enumerate(cam.get_frame_generator(limit=10, timeout_ms=3000)):
                print('Got {}'.format(frame), flush=True)

                num_bytes_per_pixel = 1  # Assuming BayerRG8 format, may change with other formats
                image_size = frame.get_width() * frame.get_height() * num_bytes_per_pixel

                raw_frame = bytearray(frame.get_buffer()[:image_size])  # Buffer may include chunk data

                # Save the raw data to a file
                raw_filename = f"frame_{i}.raw"
                with open(raw_filename, "wb") as binary_file:
                    binary_file.write(raw_frame)

                # Convert and save as DNG
                dng_filename = f"frame_{i}.dng"
                save_as_dng(raw_filename, frame.get_width(), frame.get_height(), dng_filename)
                print(f"Saved frame {i} as {dng_filename}")

if __name__ == "__main__":
    main()


pip install rawpy imageio
