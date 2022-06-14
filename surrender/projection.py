import numpy as np
from copy import deepcopy

from surrender.vector import *


def viewport_transform(vector, source, target):
    x = vector.x - source.min().x
    x /= source.max().x - source.min().x
    x *= target.max().x - target.min().x

    y = vector.y - source.min().y
    y /= source.max().y - source.min().y
    y = 1 - y
    y *= target.max().y - target.min().y

    vector.x = x
    vector.y = y
    return vector

def align_shapes_to_window(shapes, window):
    wc = window.center()
    uv = window.up_vector()
    nv = window.normal_vector()

    x_angle = vector_x_angle(nv)
    y_angle = vector_y_angle(nv) - np.pi / 2
    x_angle = 0
    z_angle = vector_z_angle(uv)

    print(f'{uv = }')
    print(f'{nv = }')
    print(f'{x_angle = }')
    print(f'{y_angle = }')
    print(f'{z_angle = }')
    print()

    for shape in shapes:
        shape = deepcopy(shape)
        shape.move(-wc)
        shape.rotate_x(x_angle)
        shape.rotate_y(y_angle)
        shape.rotate_z(z_angle)
        yield shape
