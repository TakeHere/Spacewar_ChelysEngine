import turtle

from Configs.WindowConfig import WindowConfig
from Display.Renderer import Renderer
from Utils import MathUtils


class Window:
    _instance = None
    is_in_menu = True
    _slowed_rendering = 0
    _wireframe_rendering = False

    def __init__(self, width, height, title, color):
        if self._instance is None:
            self.width = width
            self.height = height
            self.title = title
            self.color = color
            self.display_window = turtle.Screen()
            screen_width = self.display_window.getcanvas().winfo_screenwidth()
            self.display_window.setup(self.width, self.height, screen_width / 2 - self.width / 2, 0)
            self.display_window.bgcolor(color.get_hex())
            self.display_window.cv._rootwindow.resizable(False, False)
            self.display_window.title(title)
            self.renderer = Renderer()

            root = turtle.Screen()._root
            root.iconbitmap("res/logo.ico")

            self.display_window.tracer(0)
            self.display_window.onkeypress(self._toggle_wireframe, "u")
            self.display_window.onkeypress(self._faster_rendering, "i")
            self.display_window.onkeypress(self._slower_rendering, "o")
            self.display_window.onkeypress(self._reset_rendering_speed, "p")

            self._instance = self

    def update(self, fps):
        self.display_window.title(self.title + f' | FPS: {round(fps)}')
        self.display_window.update()
        Renderer.get_renderer().drawer.clear()

    def apply_color(self):
        self.display_window.bgpic("")
        self.display_window.bgcolor(self.color.get_hex())

    def _slower_rendering(self):
        self._slowed_rendering += 0.025

    def _faster_rendering(self):
        self._slowed_rendering = MathUtils.clamp(self._slowed_rendering, 0.0, 1.0)

    def _reset_rendering_speed(self):
        self._slowed_rendering = 0

    def _toggle_wireframe(self):
        self._wireframe_rendering = not self._wireframe_rendering

    @classmethod
    def get_window(cls):
        if cls._instance is None:
            cls._instance = Window(WindowConfig.WINDOW_WIDTH, WindowConfig.WINDOW_HEIGHT,
                                   WindowConfig.WINDOW_TITLE, WindowConfig.WINDOW_COLOR)

        return cls._instance
