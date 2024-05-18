from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])
Colour = namedtuple("Colour", ['R', 'G', 'B'])
Vertex = namedtuple("Vertex", ["Point", "Colour"])