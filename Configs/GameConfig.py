

class GameConfig:
    # Engine
    GRAVITY = -0.1

    # Player
    PLAYER_SPEED_ADDITION = 2
    PLAYER_VELOCITY_DECELERATION = 0.9
    PLAYER_ROTATION_SPEED = 6
    PLAYER_RECOIL = 8
    BULLET_SPEED = 15

    # GUI labels
    SCORE_TEXT = "Score: "
    HINT_TEXT = "Press SPACE to shoot !"

    # Score
    POINTS_PER_SECOND = 250
    POINTS_PER_KILL = 1000

    # Enemy
    MIN_ENEMY_SPEED = 8
    MAX_ENEMY_SPEED = 12

    SPAWN_CIRCLE_RADIUS = 800
    MIN_SPAWN_TIME = 1
    MAX_SPAWN_TIME = 3
