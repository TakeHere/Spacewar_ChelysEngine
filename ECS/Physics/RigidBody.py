from ECS.Component import Component
from Configs.GameConfig import GameConfig
from Utils.Vector2 import Vector2


class RigidBody(Component):
    def __init__(self, use_gravity):
        self.use_gravity = use_gravity
        self.velocity = Vector2(0, 0)

    def update(self, entity):
        if self.use_gravity:
            self.velocity = self.velocity.add(Vector2(0, GameConfig.GRAVITY))

        entity.position = entity.position.add(self.velocity)

    def destroy(self):
        pass
