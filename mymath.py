import math
def convert_point_for_pygame(point, width, height):
    x, y = point
    return ((x+1)*width/2, height-(y+1)*height/2)

def rotate_point(point, angle, ux, uy, uz):
    x, y, z = point
    # Axis direction (normalized): line (1,1,-1)->(-1,-1, 1)
    sq = ux*ux+uy*uy+uz*uz
    ux, uy, uz = ux/math.sqrt(sq), uy/math.sqrt(sq), uz/math.sqrt(sq)
    # Precompute trig
    c = math.cos(angle)
    s = math.sin(angle)
    oc = 1 - c
    
    # Rodrigues' rotation formula
    x_new = (ux*ux*oc + c) * x + (ux*uy*oc - uz*s) * y + (ux*uz*oc + uy*s) * z
    y_new = (uy*ux*oc + uz*s) * x + (uy*uy*oc + c) * y + (uy*uz*oc - ux*s) * z  
    z_new = (uz*ux*oc - uy*s) * x + (uz*uy*oc + ux*s) * y + (uz*uz*oc + c) * z
    
    return (x_new, y_new, z_new)

def add_distance(point):
    x, y, z = point
    return (x, y, z+3)

def project(point, width, height, angle):
    x, y, z = add_distance(rotate_point(point, angle, -1, -4, 1));
    return convert_point_for_pygame((x/z, y/z), width, height)
# 0, 0, 1 -2, -2, 1
points = [
(-1.0, -1.0, -0.5),
#(-1.0, -1.0, 0.0),
(-1.0, -1.0, 0.5),
(-1.0, -0.5, -1.0),
(-1.0, -0.5, 1.0),
#(-1.0, 0.0, -1.0),
#(-1.0, 0.0, 1.0),
(-1.0, 0.5, -1.0),
(-1.0, 0.5, 1.0),
(-1.0, 1.0, -0.5),
#(-1.0, 1.0, 0.0),
(-1.0, 1.0, 0.5),
(-0.5, -1.0, -1.0),
(-0.5, -1.0, 1.0),
(-0.5, 1.0, -1.0),
(-0.5, 1.0, 1.0),
#(0.0, -1.0, -1.0),
#(0.0, -1.0, 1.0),
#(0.0, 1.0, -1.0),
#(0.0, 1.0, 1.0),
(0.5, -1.0, -1.0),
(0.5, -1.0, 1.0),
(0.5, 1.0, -1.0),
(0.5, 1.0, 1.0),
(1.0, -1.0, -0.5),
#(1.0, -1.0, 0.0),
(1.0, -1.0, 0.5),
(1.0, -0.5, -1.0),
(1.0, -0.5, 1.0),
#(1.0, 0.0, -1.0),
#(1.0, 0.0, 1.0),
(1.0, 0.5, -1.0),
(1.0, 0.5, 1.0),
(1.0, 1.0, -0.5),
#(1.0, 1.0, 0.0),
(1.0, 1.0, 0.5)
]


