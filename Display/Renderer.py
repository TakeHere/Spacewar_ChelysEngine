import turtle


class Renderer:
    _instance = None

    def __init__(self):
        if self._instance is None:
            self.drawer = turtle.Turtle()
            self.drawer.hideturtle()
            self.drawer.penup()

            self._instance = self

    @classmethod
    def get_renderer(cls):
        if cls._instance is None:
            cls._instance = Renderer()
        return cls._instance



