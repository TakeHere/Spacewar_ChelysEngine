import math

from Display.Renderer import Renderer
from ECS.Renderable.Renderable import Renderable
from Utils.Color import Color
from Utils.Vector2 import Vector2


class Triangle(Renderable):

    def __init__(self, color, pivotpoint_offset, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.pivotpoint_offset = pivotpoint_offset

    def render(self, entity):
        position = entity.position.subtract(Vector2(self.width / 2, self.height / 3))
        rotation = entity.rotation
        pivot = entity.position.add(self.pivotpoint_offset)

        points = Renderable.get_triangle_points(self.width, self.height)

        super().render_points(points, self.color, position, pivot, rotation)
