from Display.Renderer import Renderer
from ECS.Renderable.Renderable import Renderable
from Utils.Color import Color
from Utils.Vector2 import Vector2


class BulletRenderable(Renderable):

    def __init__(self, pivotpoint_offset):
        super().__init__()
        self.pivotpoint_offset = pivotpoint_offset

    def render(self, entity):
        position = entity.position
        rotation = entity.rotation
        pivot = position.add(self.pivotpoint_offset)

        # Exterior rectangle
        points = Renderable.get_rectangle_points(15, 40)
        super().render_points(points, Color(247, 208, 15), position.add(Vector2(0, 0)), pivot, rotation)

        # Interior rectangle
        points = Renderable.get_rectangle_points(10, 20)
        super().render_points(points, Color(193, 247, 15), position.add(Vector2(0, 0)), pivot, rotation)
