from Display.Window import Window
from Utils.Vector2 import Vector2


class GuiManager:
    _instance = None
    _texts = {}

    def __init__(self):
        if self._instance is None:
            self.canvas = Window.get_window().display_window.getcanvas()
            self._instance = self

    @classmethod
    def get_guimanager(cls):
        if cls._instance is None:
            cls._instance = GuiManager()

        return cls._instance

    def add_text(self, name, text, position, color, font):
        position.y = Window.get_window().height - position.y
        screen_pos = position.to_screen_coords()
        text_object = self.canvas.create_text(screen_pos.x, screen_pos.y, text=text, fill=color, font=font, anchor="w")
        self._texts[name] = text_object

    def modify_text(self, name, new_text):
        self.canvas.itemconfig(self._texts[name], text=new_text)

    def delete_text(self, name):
        self.canvas.delete(self._texts[name])
        if name in self._texts:
            del self._texts[name]

    def hide_text(self, name):
        self.modify_text(name, "")

    def hide_all_texts(self):
        for text_name in self._texts.keys():
            self.hide_text(text_name)

    def get_text(self, name):
        self.canvas.itemcget(self._texts[name], "text")
