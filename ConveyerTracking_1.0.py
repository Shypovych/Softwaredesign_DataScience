# ConveyerTracking

import math

# Add start coordinates
start_x = float(input("Enter start X: "))
start_y = float(input("Enter start Y: "))
start_z = float(input("Enter start Z: "))
start = (start_x, start_y, start_z)

# AAdd end coordinates
end_x = float(input("Enter end X: "))
end_y = float(input("Enter end Y: "))
end_z = float(input("Enter end Z: "))
end = (end_x, end_y, end_z)

# Calculate the distance between start and end points (mm)
distance_mm = math.dist(start, end)

# Add encoder positions
pos1 = float(input("Enter starting encoder position: "))
pos2 = float(input("Enter ending encoder position: "))

# Calculate relative counts
relative_counts = pos2 - pos1

# Calculate counts per meter
counts_per_meter = relative_counts * 10000 / distance_mm

# Output results
print(f"Measured distance: {distance_mm:.2f} mm")
print(f"Relative encoder distance: {relative_counts:.2f} mm")
print(f"Counts per meter: {counts_per_meter:.2f}")