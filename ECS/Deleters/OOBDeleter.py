from Display.Window import Window
from ECS.Component import Component


class OOBDeleter(Component):
    def __init__(self):
        pass

    def update(self, entity):
        window = Window.get_window()
        x_in_window = 0 <= entity.position.x < window.width
        y_in_window = 0 <= entity.position.y < window.height

        if not (x_in_window and y_in_window):
            entity.destroy()

    def destroy(self):
        pass
