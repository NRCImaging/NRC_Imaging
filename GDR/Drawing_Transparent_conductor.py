import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Constants
big_square_size_mm = 18  # mm
num_small_squares = 6
small_square_size_mm = big_square_size_mm / num_small_squares

# Convert mm to microns for line drawing
mm_to_microns = 1000
small_square_size_microns = small_square_size_mm * mm_to_microns

# Line thicknesses in microns
vertical_thicknesses = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
horizontal_thicknesses = [7.5, 12.5, 17.5, 22.5, 27.5, 32.5, 37.5, 42.5, 47.5, 52.5, 57.5, 62.5, 67.5, 72.5]

# Line spacing in microns
vertical_spacing = 171.4285
horizontal_spacing = 187.6923

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, big_square_size_mm)
ax.set_ylim(0, big_square_size_mm)

# Draw the big square
big_square = patches.Rectangle((0, 0), big_square_size_mm, big_square_size_mm, edgecolor='black', facecolor='none')
ax.add_patch(big_square)

# Draw the small squares and lines
for i in range(num_small_squares):
    for j in range(num_small_squares):
        x0 = i * small_square_size_mm
        y0 = j * small_square_size_mm
        
        # Draw the small square
        small_square = patches.Rectangle((x0, y0), small_square_size_mm, small_square_size_mm, edgecolor='black', facecolor='none')
        ax.add_patch(small_square)
        
        # Draw vertical lines
        for k, thickness in enumerate(vertical_thicknesses):
            x = x0 + k * vertical_spacing / mm_to_microns
            if x < x0 + small_square_size_mm:
                ax.add_line(plt.Line2D((x, x), (y0, y0 + small_square_size_mm), color='black', linewidth=thickness / mm_to_microns))
        
        # Draw horizontal lines
        for k, thickness in enumerate(horizontal_thicknesses):
            y = y0 + k * horizontal_spacing / mm_to_microns
            if y < y0 + small_square_size_mm:
                ax.add_line(plt.Line2D((x0, x0 + small_square_size_mm), (y, y), color='black', linewidth=thickness / mm_to_microns))

# Draw the circle
circle_diameter_cm = 1.8  # cm
circle_radius_mm = (circle_diameter_cm * 10) / 2  # convert cm to mm and divide by 2 for radius
circle = patches.Circle((big_square_size_mm / 2, big_square_size_mm / 2), circle_radius_mm, edgecolor='black', facecolor='none')
ax.add_patch(circle)

# Set equal scaling
ax.set_aspect('equal')
plt.gca().invert_yaxis()
plt.show()
