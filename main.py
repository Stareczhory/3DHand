from vpython import *

scene.title = "3D Scene from PyCharm"

wrist = (0,0,0)
index_mcp = (-1.5,2,0)
middle_mcp = (-0.5,2,0)
ring_mcp = (0.5,2,0)
pinky_mcp = (1.5, 2, 0)
index_tip = (-1.5,4,0)
middle_tip = (-0.5,4,0)
ring_tip = (0.5,4,0)
pinky_tip = (1.5, 4, 0)

points(pos=[wrist, index_mcp, middle_mcp, ring_mcp, pinky_mcp, index_tip,middle_tip,ring_tip,pinky_tip])

wrist_index_mcp_line = cylinder(pos=vector(*wrist), axis=vector(*index_mcp)-vector(*wrist), radius=0.05, color=color.cyan)
wrist_middle_mcp_line = cylinder(pos=vector(*wrist), axis=vector(*middle_mcp)-vector(*wrist), radius=0.05, color=color.cyan)
wrist_ring_mcp_line = cylinder(pos=vector(*wrist), axis=vector(*ring_mcp)-vector(*wrist), radius=0.05, color=color.cyan)
wrist_pinky_mcp_line = cylinder(pos=vector(*wrist), axis=vector(*pinky_mcp)-vector(*wrist), radius=0.05, color=color.cyan)

index_mcp_index_tip_line = cylinder(pos=vector(*index_mcp), axis=vector(*index_tip)-vector(*index_mcp), radius=0.05, color=color.cyan)
middle_mcp_middle_tip_line = cylinder(pos=vector(*middle_mcp), axis=vector(*middle_tip)-vector(*middle_mcp), radius=0.05, color=color.cyan)
ring_mcp_ring_tip_line = cylinder(pos=vector(*ring_mcp), axis=vector(*ring_tip)-vector(*ring_mcp), radius=0.05, color=color.cyan)
pinky_mcp_pinky_tip_line = cylinder(pos=vector(*pinky_mcp), axis=vector(*pinky_tip)-vector(*pinky_mcp), radius=0.05, color=color.cyan)

# Keep the scene alive
while True:
    rate(60)  # 60 frames per second
