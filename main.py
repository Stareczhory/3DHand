import csv
from operator import index
import time

from vpython import *
import pandas as pd

scene.title = "3D Scene from PyCharm"

path = r'C:\Users\jakub\PycharmProjects\Data Processing\tracking_data.csv'

rows = []

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 8:
            rows.append(row[:8:2])  # Take only every second value
        # Else: skip the row or log a warning


data = pd.DataFrame(rows).astype('int')

wrist = vector(0,0,0)
index_mcp = vector(-1.5,4,0)
middle_mcp = vector(-0.5,4,0)
ring_mcp = vector(0.5,4,0)
pinky_mcp = vector(1.5, 4, 0)
index_tip = vector(-1.5,7,0)
middle_tip = vector(-0.5,7,0)
ring_tip = vector(0.5,7,0)
pinky_tip = vector(1.5, 7, 0)

# index_pip = vector(-1.5,5,0)
# middle_pip = vector(-0.5,5,0)
# ring_pip = vector(0.5,5,0)
# pinky_pip = vector(1.5, 5, 0)
#
# index_dip = vector(-1.5,6,0)
# middle_dip = vector(-0.5,6,0)
# ring_dip = vector(0.5,6,0)
# pinky_dip = vector(1.5, 6, 0)

tip_vectors = [index_tip, middle_tip, ring_tip, pinky_tip]

hand_points = points(pos=[wrist, index_mcp, middle_mcp, ring_mcp, pinky_mcp])

wrist_index_mcp_line = cylinder(pos=wrist, axis=index_mcp - wrist, radius=0.05, color=color.cyan)
wrist_middle_mcp_line = cylinder(pos=wrist, axis=middle_mcp - wrist, radius=0.05, color=color.cyan)
wrist_ring_mcp_line = cylinder(pos=wrist, axis=ring_mcp - wrist, radius=0.05, color=color.cyan)
wrist_pinky_mcp_line = cylinder(pos=wrist, axis=pinky_mcp - wrist, radius=0.05, color=color.cyan)

index_mcp_index_tip_line = cylinder(pos=index_mcp, axis=index_tip - index_mcp, radius=0.05, color=color.cyan)
middle_mcp_middle_tip_line = cylinder(pos=middle_mcp, axis=middle_tip - middle_mcp, radius=0.05, color=color.cyan)
ring_mcp_ring_tip_line = cylinder(pos=ring_mcp, axis=ring_tip - ring_mcp, radius=0.05, color=color.cyan)
pinky_mcp_pinky_tip_line = cylinder(pos=pinky_mcp, axis=pinky_tip - pinky_mcp, radius=0.05, color=color.cyan)

for i, row in data.iterrows():
    rate(20)
    angles = row
    for idx, angle in enumerate(angles):

        tip_coords = tip_vectors[idx]

        length_a = 4
        length_b = 3
        length_c = sqrt(length_a**2 + length_b**2 - 2*length_a*length_b*cos(radians(angle)))
        z_coordinate = sqrt(length_b**2 - ((length_c**2 - length_b**2 + length_a**2)/(2*length_a)-length_a)**2)
        y_coordinate = (length_c**2 - length_b**2 + length_a**2)/(2*length_a)

        tip_coords.y = y_coordinate
        tip_coords.z = z_coordinate

    index_mcp_index_tip_line.axis = index_tip - index_mcp
    middle_mcp_middle_tip_line.axis = middle_tip - middle_mcp
    ring_mcp_ring_tip_line.axis = ring_tip - ring_mcp
    pinky_mcp_pinky_tip_line.axis = pinky_tip - pinky_mcp


