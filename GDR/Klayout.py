# Import the necessary KLayout modules
import klayout.db as db

# Create a new layout
layout = db.Layout()

# Create a new layer
layer = layout.layer(1, 0)

# Create a new cell
top_cell = layout.create_cell("TOP")

# Define the starting x-coordinate for the first line
start_x = 0

# Define the thicknesses and spacing
thicknesses = range(5, 80, 5)  # 5, 10, 15, ..., 75 microns
spacing = 160  # 160 microns

# Loop through each thickness and create a vertical line
for thickness in thicknesses:
    # Create a vertical line (rectangle) with the specified thickness
    points = [
        db.Point(start_x, 0),
        db.Point(start_x + thickness, 0),
        db.Point(start_x + thickness, 10000),  # 10,000 microns tall
        db.Point(start_x, 10000)
    ]
    polygon = db.Polygon(points)
    
    # Insert the polygon into the cell on the specified layer
    top_cell.shapes(layer).insert(polygon)
    
    # Update the starting x-coordinate for the next line
    start_x += thickness + spacing

# Save the layout to a GDS file
layout.write("vertical_lines.gds")
