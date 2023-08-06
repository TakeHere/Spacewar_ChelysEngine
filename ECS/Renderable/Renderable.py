import math
from time import sleep

from Display.Renderer import Renderer
from Display.Window import Window
from ECS.Component import Component
from abc import ABC, abstractmethod

from Utils.Vector2 import Vector2

_renderables = []


def list_renderables():
    return _renderables


class Renderable(Component):

    def __init__(self):
        _renderables.append(self)

    @abstractmethod
    def render(self, entity):
        pass

    def update(self, entity):
        self.render(entity)

    def destroy(self):
        _renderables.remove(self)

    @staticmethod
    def get_circle_points(num_points, radius):
        angle_increment = 2 * math.pi / num_points
        points = []
        for i in range(num_points):
            angle = i * angle_increment
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            points.append(Vector2(x, y))
        points.append(points[0])

        return points

    @staticmethod
    def get_triangle_points(width, height):
        return (
            Vector2(0, 0),
            Vector2(width, 0),
            Vector2(width / 2, height),
            Vector2(0, 0)
        )

    @staticmethod
    def get_rectangle_points(width, height):
        half_width = width / 2
        half_height = height / 2

        return (Vector2(-half_width, half_height), Vector2(half_width, half_height),
                Vector2(half_width, -half_height), Vector2(-half_width, -half_height),
                Vector2(-half_width, half_height))

    def render_points(self, points, color, position, pivot, rotation):
        drawer = Renderer.get_renderer().drawer
        window = Window.get_window()

        if window._wireframe_rendering:
            drawer.pendown()
        else:
            drawer.penup()

        drawer.pensize(2)
        drawer.fillcolor(color.get_hex())
        drawer.begin_fill()

        for point in points:
            world_point = point.add(position)
            rotated_point = world_point.rotate_around_point(pivot, rotation)
            drawer.goto(rotated_point.to_turtle())


        drawer.end_fill()

        if window._slowed_rendering != 0:
            window.display_window.update()
            sleep(window._slowed_rendering)

