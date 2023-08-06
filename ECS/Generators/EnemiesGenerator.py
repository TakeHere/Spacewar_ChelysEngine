import math
import random
import time

import ScoreManager
from Display.Window import Window
from ECS.Deleters.DeletionTimer import DeletionTimer
from ECS.Entity import Entity
from ECS.Physics.Collidable import Collidable
from ECS.Physics.RigidBody import RigidBody
from ECS.Renderable.DisplacedCircle import DisplacedCircle
from Configs.GameConfig import GameConfig
from Utils import MathUtils
from Utils.Color import Color
from Utils.Vector2 import Vector2


def generate_enemy(player):
    # Generate enemy position
    window = Window.get_window()
    angle = random.uniform(0, 360)
    random_location = Vector2(
        math.sin(math.radians(angle)) * GameConfig.SPAWN_CIRCLE_RADIUS,
        math.cos(math.radians(angle)) * GameConfig.SPAWN_CIRCLE_RADIUS * -1
    ).add(Vector2(window.width / 2, window.height / 2))

    # Create the enemy
    rigidbody = RigidBody(False)
    enemy = Entity("enemy", random_location, 0)
    enemy.add_component(DisplacedCircle(Vector2(0, 0), Color(41, 17, 3), 10, 3, 20))
    enemy.add_component(rigidbody)
    enemy.add_component(DeletionTimer(5))
    enemy.add_component(Collidable(enemy.position, 40, 40))

    rigidbody.velocity = player.position.subtract(enemy.position).normalize().multiply(random.uniform(
        GameConfig.MIN_ENEMY_SPEED, GameConfig.MAX_ENEMY_SPEED))


_next_spawn = time.time() + GameConfig.MAX_SPAWN_TIME


def enemy_spawner_timer(player):
    global _next_spawn

    if time.time() >= _next_spawn:
        generate_enemy(player)
        t = MathUtils.clamp(ScoreManager.get_score() / 15000, 0.0, 1.0)
        wait_time = MathUtils.map_range(t, 0.0, 1.0, 3.0, 1.0)
        _next_spawn = time.time() + wait_time #random.uniform(GameConfig.MIN_SPAWN_TIME, GameConfig.MAX_SPAWN_TIME)
