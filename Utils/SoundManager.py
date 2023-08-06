import threading

import winsound

from Display.Window import Window
from Utils.Vector2 import Vector2


class SoundManager:
    _instance = None
    _sounds = {}

    def __init__(self):
        if self._instance is None:
            self._instance = self

    @classmethod
    def get_soundmanager(cls):
        if cls._instance is None:
            cls._instance = SoundManager()

        return cls._instance

    def add_sound(self, name, path):
        self._sounds[name] = path

    def delete_sound(self, name):
        if name in self._sounds:
            del self._sounds[name]

    def play_sound(self, name, loop=False):

        path = self._sounds[name]

        sound_thread = threading.Thread(target=_play_sound, args=(loop, path,))
        sound_thread.daemon = True
        sound_thread.start()


def _play_sound(loop, path):
    if loop:
        while True:
            winsound.PlaySound(path, winsound.SND_FILENAME)
    else:
        winsound.PlaySound(path, winsound.SND_FILENAME)

