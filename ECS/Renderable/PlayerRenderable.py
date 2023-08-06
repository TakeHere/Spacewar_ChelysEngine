from Display.Renderer import Renderer
from ECS.Renderable.Renderable import Renderable
from Utils.Color import Color
from Utils.Vector2 import Vector2


class PlayerRenderable(Renderable):

    def __init__(self, pivotpoint_offset):
        super().__init__()
        self.pivotpoint_offset = pivotpoint_offset

    def render(self, entity):
        position = entity.position
        rotation = entity.rotation
        pivot = position.add(self.pivotpoint_offset)

        points = Renderable.get_circle_points(15, 10)
        super().render_points(points, Color(14, 71, 6), position.add(Vector2(25 + 5, -10)), pivot, rotation)

        points = Renderable.get_circle_points(15, 10)
        super().render_points(points, Color(14, 71, 6), position.add(Vector2(-(25 + 5), -10)), pivot, rotation)

        points = Renderable.get_circle_points(25, 30)
        super().render_points(points, Color(14, 71, 6), position.add(Vector2(0, 0)), pivot, rotation)

        # Main rectangle body
        points = Renderable.get_rectangle_points(50, 20)
        super().render_points(points, Color(14, 71, 6), position.add(Vector2(0, 0)), pivot, rotation)

        # Upper triangle exterior
        points = Renderable.get_triangle_points(50, 80)
        super().render_points(points, Color(43, 224, 20),
                              position.subtract(Vector2(50 / 2, 80 / 3)).add(Vector2(0, 40)), pivot, rotation)

        # Upper triangle interior
        points = Renderable.get_triangle_points(30, 50)
        super().render_points(points, Color(34, 176, 14),
                              position.subtract(Vector2(30 / 2, 50 / 3)).add(Vector2(0, 29)), pivot, rotation)

        # Right rectangle gun
        points = Renderable.get_rectangle_points(15, 40)
        super().render_points(points, Color(14, 71, 6), position.add(Vector2(25+7, 20 - 10)), pivot, rotation)

        # Left rectangle gun
        points = Renderable.get_rectangle_points(15, 40)
        super().render_points(points, Color(14, 71, 6), position.add(Vector2(- (25 + 7), 20 - 10)), pivot, rotation)

        # Right rectangle gun top
        points = Renderable.get_triangle_points(15, 15)
        super().render_points(points, Color(174, 191, 17),
                              position.subtract(Vector2(50 / 2, 60 / 3)).add(Vector2(25 + 7 + 18, 20 + 29)), pivot, rotation)

        # Left rectangle gun top
        points = Renderable.get_triangle_points(15, 15)
        super().render_points(points, Color(174, 191, 17),
                              position.subtract(Vector2(50 / 2, 60 / 3)).add(Vector2(-(25 + 7) + 18, 20 + 29)), pivot,
                              rotation)

        '''
        OLD
        
        # Draw main triangle
        points = Renderable.get_triangle_points(60, 60)
        super().render_points(points, Color(27, 128, 14), position.subtract(Vector2(40 / 2, 20 / 3)).subtract(Vector2(10, 0)), pivot, rotation)

        # Draw rectangle body
        points = Renderable.get_rectangle_points(60, 10)
        super().render_points(points, Color(14, 71, 6), position.add(Vector2(0, -8)), pivot, rotation)

        # Draw left circle
        points = Renderable.get_circle_points(20, 12)
        super().render_points(points, Color(118, 173, 35), position.add(Vector2(-20, -6)), pivot, rotation)

        # Draw right circle
        points = Renderable.get_circle_points(20, 12)
        super().render_points(points, Color(118, 173, 35), position.add(Vector2(20, -6)), pivot, rotation)
        '''