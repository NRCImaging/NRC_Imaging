from PIL import Image

def convert_tif_to_png(tif_path, png_path):
    try:
        # Open the TIFF image
        with Image.open(tif_path) as img:
            # Save as PNG
            img.save(png_path, format="PNG")
        print("Conversion completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Paths to input and output files
tif_file = "/Users/ebrahimgdr/Downloads/frontside.tif"
png_file = "brokenother.png"

# Convert TIFF to PNG
convert_tif_to_png(tif_file, png_file)
