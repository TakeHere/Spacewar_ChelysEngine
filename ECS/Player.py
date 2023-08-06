from Display.Window import Window
from ECS.Entity import Entity
from ECS.Generators.ParticleSystem import ParticleSystem
from ECS.Physics.Collidable import Collidable
from ECS.Deleters.OOBDeleter import OOBDeleter
from ECS.Physics.RigidBody import RigidBody
from ECS.Renderable.BulletRenderable import BulletRenderable
from ECS.Renderable.Circle import Circle
from ECS.Renderable.PlayerRenderable import PlayerRenderable
from Configs.GameConfig import GameConfig
from Utils.SoundManager import SoundManager
from Utils.InputManager import InputManager
from Utils import MathUtils
from Utils.Color import Color
from Utils.Vector2 import Vector2


class Player(Entity):
    def __init__(self, name, position, rotation):
        super().__init__(name, position, rotation)

        self.add_component(RigidBody(False))
        self.add_component(PlayerRenderable(Vector2(0, 0)))
        self.add_component(Collidable(self.position, 70, 70))
        self.input_manager = InputManager.get_inputmanager()
        self.particle_generator = ParticleSystem(self.position,
                                                 Circle(Color(100, 100, 100), Vector2(0, 0), 5, 8),
                                                 5, 1, False, 1, 3)

        Window.get_window().display_window.onkey(self.shoot, "space")

    def update(self):
        self.movement()

    def movement(self):
        # Player rotation
        if self.input_manager.is_pressed("Left"):
            self.rotation += GameConfig.PLAYER_ROTATION_SPEED
        elif self.input_manager.is_pressed("Right"):
            self.rotation -= GameConfig.PLAYER_ROTATION_SPEED

        # Player acceleration
        rigidbody = self.get_component(RigidBody)
        if self.input_manager.is_pressed("Up"):
            rigidbody.velocity = rigidbody.velocity.add(
                MathUtils.get_forward_vector(self.rotation).multiply(-1).multiply(GameConfig.PLAYER_SPEED_ADDITION))
        elif self.input_manager.is_pressed("Down"):
            rigidbody.velocity = rigidbody.velocity.add(
                MathUtils.get_forward_vector(self.rotation).multiply(GameConfig.PLAYER_SPEED_ADDITION))

        # Player friction
        rigidbody.velocity = rigidbody.velocity.multiply(GameConfig.PLAYER_VELOCITY_DECELERATION)

        # Player teleportation if OOB
        window = Window.get_window()
        if self.position.x > window.width: self.position.x = 0
        if self.position.x < 0: self.position.x = window.width
        if self.position.y > window.height: self.position.y = 0
        if self.position.y < 0: self.position.y = window.height

    def shoot(self):
        if not Window.is_in_menu:
            # Find shoot position
            relative_position = Vector2(0, 60)
            world_position = relative_position.add(self.position)
            rotated_position = world_position.rotate_around_point(self.position, self.rotation)

            # Player recoil
            rigidbody = self.get_component(RigidBody)

            rigidbody.velocity = rigidbody.velocity.add(
                MathUtils.get_forward_vector(self.rotation).multiply(GameConfig.PLAYER_RECOIL))

            # Particles
            self.particle_generator.position = rotated_position
            self.particle_generator.generate()

            # Create bullet
            bullet = Entity("bullet", rotated_position, self.rotation)
            bullet.add_component(BulletRenderable(Vector2(0, 0)))
            bullet.add_component(RigidBody(False))
            bullet.add_component(OOBDeleter())
            bullet.add_component(Collidable(bullet.position, 50, 50))

            # Accelerates towards player
            bullet_rigidbody = bullet.get_component(RigidBody)
            bullet_rigidbody.velocity = MathUtils.get_forward_vector(self.rotation).multiply(-1).multiply(
                GameConfig.BULLET_SPEED)

            # Play sound
            SoundManager.get_soundmanager().play_sound("shoot", False)
