from Display.Renderer import Renderer
from ECS.Renderable.Renderable import Renderable
from Utils.Color import Color
from Utils.Vector2 import Vector2


class Rectangle(Renderable):

    def __init__(self, color, pivotpoint_offset, height, width):
        super().__init__()
        self.height = height
        self.width = width
        self.color = color
        self.pivotpoint_offset = pivotpoint_offset

    def render(self, entity):
        position = entity.position
        rotation = entity.rotation
        pivot = position.add(self.pivotpoint_offset)

        points = Renderable.get_rectangle_points(self.width, self.height)

        super().render_points(points, self.color, position, pivot, rotation)
