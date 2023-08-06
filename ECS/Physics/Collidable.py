from ECS.Component import Component

_collidables = []


class Collidable(Component):
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height
        _collidables.append(self)

    def update(self, entity):
        self.position = entity.position

    def is_colliding(self, collidable2):
        return (
                self.position.x < collidable2.position.x + collidable2.width and
                self.position.x + self.width > collidable2.position.x and
                self.position.y < collidable2.position.y + collidable2.height and
                self.position.y + self.height > collidable2.position.y
        )

    def destroy(self):
        _collidables.remove(self)
