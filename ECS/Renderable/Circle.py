import math
from Display.Renderer import Renderer
from ECS.Renderable.Renderable import Renderable
from Utils.Color import Color
from Utils.Vector2 import Vector2


class Circle(Renderable):

    def __init__(self, color, pivotpoint_offset, radius, points_amount):
        super().__init__()
        self.radius = radius
        self.color = color
        self.pivotpoint_offset = pivotpoint_offset
        self.points_amount = points_amount

    def render(self, entity):
        position = entity.position
        rotation = entity.rotation
        pivot = position.add(self.pivotpoint_offset)

        points = Renderable.get_circle_points(self.points_amount, self.radius)

        super().render_points(points, self.color, position, pivot, rotation)
