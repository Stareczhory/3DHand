import csv
from operator import index
import time
import numpy as np

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

cylinder_radius = 0.15

wrist = vector(0,0,0)

index_mcp = vector(-1.5,4,0)
middle_mcp = vector(-0.5,4,0)
ring_mcp = vector(0.5,4,0)
pinky_mcp = vector(1.5, 4, 0)

index_tip = vector(-1.5,7,0)
middle_tip = vector(-0.5,7,0)
ring_tip = vector(0.5,7,0)
pinky_tip = vector(1.5, 7, 0)

index_pip = vector(-1.5,5,0)
middle_pip = vector(-0.5,5,0)
ring_pip = vector(0.5,5,0)
pinky_pip = vector(1.5, 5, 0)

index_dip = vector(-1.5,6,0)
middle_dip = vector(-0.5,6,0)
ring_dip = vector(0.5,6,0)
pinky_dip = vector(1.5, 6, 0)

tip_vectors = [index_tip, middle_tip, ring_tip, pinky_tip]
dip_vectors = [index_dip, middle_dip, ring_dip, pinky_dip]
pip_vectors = [index_pip, middle_pip, ring_pip, pinky_pip]

hand_points = points(pos=[wrist, index_mcp, middle_mcp, ring_mcp, pinky_mcp])

wrist_index_mcp_line = cylinder(pos=wrist, axis=index_mcp - wrist, radius=cylinder_radius, color=color.cyan)
wrist_middle_mcp_line = cylinder(pos=wrist, axis=middle_mcp - wrist, radius=cylinder_radius, color=color.cyan)
wrist_ring_mcp_line = cylinder(pos=wrist, axis=ring_mcp - wrist, radius=cylinder_radius, color=color.cyan)
wrist_pinky_mcp_line = cylinder(pos=wrist, axis=pinky_mcp - wrist, radius=cylinder_radius, color=color.cyan)

index_mcp_index_pip_line = cylinder(pos=index_mcp, axis=index_pip - index_mcp, radius=cylinder_radius, color=color.cyan)
middle_mcp_middle_pip_line = cylinder(pos=middle_mcp, axis=middle_pip - middle_mcp, radius=cylinder_radius, color=color.cyan)
ring_mcp_ring_pip_line = cylinder(pos=ring_mcp, axis=ring_pip - ring_mcp, radius=cylinder_radius, color=color.cyan)
pinky_mcp_pinky_pip_line = cylinder(pos=pinky_mcp, axis=pinky_pip - pinky_mcp, radius=cylinder_radius, color=color.cyan)

index_pip_dip_line = cylinder(pos=index_pip, axis=index_dip - index_pip, radius=cylinder_radius, color=color.cyan)
middle_pip_dip_line = cylinder(pos=middle_pip, axis=middle_dip - middle_pip, radius=cylinder_radius, color=color.cyan)
ring_pip_dip_line = cylinder(pos=ring_pip, axis=ring_dip - ring_pip, radius=cylinder_radius, color=color.cyan)
pinky_pip_dip_line = cylinder(pos=pinky_pip, axis=pinky_dip - pinky_pip, radius=cylinder_radius, color=color.cyan)

index_dip_tip_line = cylinder(pos=index_dip, axis=index_tip - index_dip, radius=cylinder_radius, color=color.cyan)
middle_dip_tip_line = cylinder(pos=middle_dip, axis=middle_tip - middle_dip, radius=cylinder_radius, color=color.cyan)
ring_dip_tip_line = cylinder(pos=ring_dip, axis=ring_tip - ring_dip, radius=cylinder_radius, color=color.cyan)
pinky_dip_tip_line = cylinder(pos=pinky_dip, axis=pinky_tip - pinky_dip, radius=cylinder_radius, color=color.cyan)

for i, row in data.iterrows():
    rate(20)
    angles = row.values

    for idx, angle in enumerate(angles):

        temp_y = 4
        temp_z = 0
        theta = 0

        tip_coords = tip_vectors[idx]
        dip_coords = dip_vectors[idx]
        pip_coords = pip_vectors[idx]

        finger_coords = [pip_coords, dip_coords, tip_coords]
        for o, coords in enumerate(finger_coords):
            if o == 0:
                temp_angle = 90 + int(angle / 2)
                theta += radians(270-temp_angle)  # cumulative angle
                coords.y = temp_y + sin(theta)
                coords.z = temp_z + cos(theta)
            elif o == 1:
                temp_angle = 90 + int(angle / 2)
                theta += radians(180-temp_angle)  # cumulative angle
                coords.y = temp_y + sin(theta)
                coords.z = temp_z + cos(theta)
            elif o == 2:
                temp_angle = 150 + int(angle / 6)
                theta += radians(180-temp_angle)  # cumulative angle
                coords.y = temp_y + sin(theta)
                coords.z = temp_z + cos(theta)

            temp_y = coords.y
            temp_z = coords.z

    index_mcp_index_pip_line.axis = index_pip - index_mcp
    middle_mcp_middle_pip_line.axis = middle_pip - middle_mcp
    ring_mcp_ring_pip_line.axis = ring_pip - ring_mcp
    pinky_mcp_pinky_pip_line.axis = pinky_pip - pinky_mcp

    index_pip_dip_line.pos = index_pip
    index_pip_dip_line.axis = index_dip - index_pip
    middle_pip_dip_line.pos = middle_pip
    middle_pip_dip_line.axis = middle_dip - middle_pip
    ring_pip_dip_line.pos = ring_pip
    ring_pip_dip_line.axis = ring_dip - ring_pip
    pinky_pip_dip_line.pos = pinky_pip
    pinky_pip_dip_line.axis = pinky_dip - pinky_pip

    index_dip_tip_line.pos = index_dip
    index_dip_tip_line.axis = index_tip - index_dip
    middle_dip_tip_line.pos = middle_dip
    middle_dip_tip_line.axis = middle_tip - middle_dip
    ring_dip_tip_line.pos = ring_dip
    ring_dip_tip_line.axis = ring_tip - ring_dip
    pinky_dip_tip_line.pos = pinky_dip
    pinky_dip_tip_line.axis = pinky_tip - pinky_dip