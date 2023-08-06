import math
import random

from Display.Renderer import Renderer
from ECS.Renderable.Renderable import Renderable
from Utils.Color import Color
from Utils.Vector2 import Vector2


class DisplacedCircle(Renderable):

    def __init__(self, pivotpoint_offset, color, radius, displacement_factor, num_points):
        super().__init__()
        self.pivotpoint_offset = pivotpoint_offset
        self.color = color
        self.radius = radius
        self.displacement_factor = displacement_factor
        self.num_points = num_points
        self.points = self.get_points(radius, displacement_factor, num_points)

    def render(self, entity):
        position = entity.position
        rotation = entity.rotation
        pivot = position.add(self.pivotpoint_offset)

        points = self.points
        super().render_points(points, self.color, position.add(Vector2(0, 0)), pivot, rotation)

    def get_points(self, radius, displacement_factor, num_points):
        points = []

        angle_increment = 2 * math.pi / num_points
        for i in range(num_points):
            angle = i * angle_increment
            x = radius * math.cos(angle) * (1 + random.random()) * displacement_factor
            y = radius * math.sin(angle) * (1 + random.random()) * displacement_factor
            points.append(Vector2(x, y))
        points.append(points[0])

        return points
