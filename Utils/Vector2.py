import math

from Configs.WindowConfig import WindowConfig


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        magnitude = self.magnitude()
        return Vector2(self.x / magnitude, self.y / magnitude)

    def add(self, vector2):
        return Vector2(self.x + vector2.x, self.y + vector2.y)

    def subtract(self, term):
        return Vector2(self.x - term.x, self.y - term.y)

    def multiply(self, factor):
        return Vector2(self.x * factor, self.y * factor)

    def divide(self, divisor):
        return Vector2(self.x / divisor, self.y / divisor)

    def to_tuple(self):
        return self.x, self.y

    def to_screen_coords(self):
        width = WindowConfig.WINDOW_WIDTH
        height = WindowConfig.WINDOW_HEIGHT

        return Vector2(self.x - width/2, self.y - height/2)

    def to_turtle(self):
        return self.to_screen_coords().to_tuple()

    def rotate_around_point(self, center, angle):
        theta = math.radians(angle)

        # Translate le point pour le centrer autour de l'origine (0, 0)
        translated_x = self.x - center.x
        translated_y = self.y - center.y

        # Effectue la rotation autour de l'origine
        rotated_x = math.cos(theta) * translated_x - math.sin(theta) * translated_y
        rotated_y = math.sin(theta) * translated_x + math.cos(theta) * translated_y

        # Translate le point de retour à sa position d'origine
        final_x = rotated_x + center.x
        final_y = rotated_y + center.y

        return Vector2(final_x, final_y)

    def log(self):
        print("[x:", self.x, "] [y:", self.y, "] [magnitude:", self.magnitude(), "] [normalized:", self.normalize().x,
              ",", self.normalize().y, "]")
