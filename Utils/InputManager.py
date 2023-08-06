from Display.Window import Window


class InputManager:
    _pressed_keys = []
    _instance = None

    def __init__(self):
        if self._instance is None:
            self.init_keys()
            self._instance = self

    @classmethod
    def get_inputmanager(cls):
        if cls._instance is None:
            cls._instance = InputManager()

        return cls._instance

    def init_keys(self):
        display = Window.get_window().display_window

        _inputs = (
            "space",
            "Up",
            "Down",
            "Left",
            "Right",
        )

        for input_name in _inputs:
            display.onkeypress(lambda input_name=input_name: self.key_pressed(input_name), input_name)
            display.onkeyrelease(lambda input_name=input_name: self.key_removed(input_name), input_name)
            display.listen()

    def key_pressed(self, input_name):
        if input_name not in self._pressed_keys:
            self._pressed_keys.append(input_name)

    def key_removed(self, input_name):
        if input_name in self._pressed_keys:
            self._pressed_keys.remove(input_name)

    def is_pressed(self, input_name):
        return input_name in self._pressed_keys


