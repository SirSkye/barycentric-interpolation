from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])
Colour = namedtuple("Colour", ['r', 'g', 'b'])
Vertex = namedtuple("Vertex", ["point", "colour"])
BarycentricPoint = namedtuple("Bary", ["alpha", "beta", "gamma"])