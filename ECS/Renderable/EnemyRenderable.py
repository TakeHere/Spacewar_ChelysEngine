import math
import random

from Display.Renderer import Renderer
from ECS.Renderable.Renderable import Renderable
from Utils.Color import Color
from Utils.Vector2 import Vector2


class EnemyRenderable(Renderable):

    def __init__(self, pivotpoint_offset):
        super().__init__()
        self.pivotpoint_offset = pivotpoint_offset
        self.points = self.get_points()

    def render(self, entity):
        position = entity.position
        rotation = entity.rotation
        pivot = position.add(self.pivotpoint_offset)

        points = self.points
        super().render_points(points, Color(41, 17, 3), position.add(Vector2(0, 0)), pivot, rotation)

    def get_points(self):
        num_points = 20
        radius = 10
        displacement_factor = 3
        points = []

        angle_increment = 2 * math.pi / num_points
        for i in range(num_points):
            angle = i * angle_increment
            x = radius * math.cos(angle) * (1 + random.random()) * displacement_factor
            y = radius * math.sin(angle) * (1 + random.random()) * displacement_factor
            points.append(Vector2(x, y))
        points.append(points[0])

        return points
