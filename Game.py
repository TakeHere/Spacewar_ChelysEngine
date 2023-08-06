import time

import ScoreManager
from Configs.GameConfig import GameConfig
from Display.GuiManager import GuiManager
from ECS.Generators.ParticleSystem import ParticleSystem
from ECS.Physics.Collidable import Collidable
from ECS.Player import Player
from ECS.Renderable.DisplacedCircle import DisplacedCircle
from Utils.SoundManager import SoundManager
from Utils.InputManager import InputManager
from Configs.WindowConfig import WindowConfig
from Display.Window import Window
from ECS import Entity
from ECS.Generators import EnemiesGenerator
from Utils.Color import Color
from Utils.Vector2 import Vector2
from typing import Optional

player: Optional[Player] = None
input_manager: Optional[InputManager] = None
enemy_death_particle_gen: Optional[ParticleSystem] = None

_last_score_give = time.time()

window = Window.get_window()
canvas = window.display_window.getcanvas()
gui_manager = GuiManager.get_guimanager()

gui_manager.add_text("score", "", Vector2(50, window.height - 50), "Yellow", "Bahnschrift 20 bold")
gui_manager.add_text("hint", "", Vector2(50, window.height - 100), "Yellow", "Bahnschrift 15 bold")

sound_manager = SoundManager.get_soundmanager()
sound_manager.add_sound("shoot", "res/sounds/shoot.wav")
sound_manager.add_sound("enemy_death", "res/sounds/enemy_explosion.wav")
sound_manager.add_sound("player_death", "res/sounds/player_explosion.wav")


def init():
    gui_manager.modify_text("score", GameConfig.SCORE_TEXT + str(ScoreManager.get_score()))
    gui_manager.modify_text("hint", GameConfig.HINT_TEXT)

    global player, input_manager, enemy_death_particle_gen

    player = Player("player", Vector2(500, 500), 0)
    input_manager = InputManager.get_inputmanager()
    enemy_death_particle_gen = ParticleSystem(Vector2(0, 0),
                                              DisplacedCircle(Vector2(0, 0), Color(173, 79, 12), 2.5, 3, 10),
                                              4, 1.5, False, 1, 1.5)

    # player.add_component(Rectangle(Color(5, 5, 80), Vector2(0, 0), 10, 10))

    '''
    player.add_component(Rectangle(Color(5, 5, 80), Vector2(0, 0), 50, 100))
    test.add_component(Rectangle(Color(5, 5, 80), Vector2(0, 0), 10, 10))
    '''


def update():
    score_management()

    gui_manager.modify_text("score", GameConfig.SCORE_TEXT + str(ScoreManager.get_score()))

    player.update()
    EnemiesGenerator.enemy_spawner_timer(player)

    drawer = Window.get_window().renderer.drawer
    drawer.goto(0, 0)

    # Destroy enemy when shoot
    for enemy in Entity.get_entities_named("enemy"):
        if enemy.has_component(Collidable):
            enemy_collidable = enemy.get_component(Collidable)
        else:
            continue
        for bullet in Entity.get_entities_named("bullet"):
            if bullet.has_component(Collidable):
                bullet_collidable = bullet.get_component(Collidable)
                if bullet_collidable.is_colliding(enemy_collidable):
                    # Bullet touched enemy
                    enemy_death_particle_gen.position = enemy.position
                    enemy_death_particle_gen.generate()
                    enemy.destroy()

                    # Play sound
                    SoundManager.get_soundmanager().play_sound("enemy_death", False)

                    # Score management
                    ScoreManager.add_to_score(GameConfig.POINTS_PER_KILL)
                    break

    # Player death when enemy collision
    if player.has_component(Collidable):
        for enemy in Entity.get_entities_named("enemy"):
            if enemy.has_component(Collidable):
                enemy_collidable = enemy.get_component(Collidable)
                player_collidable = player.get_component(Collidable)

                if player_collidable.is_colliding(enemy_collidable):
                    # Player collides with an enemy
                    for entity in Entity.list_entities():
                        entity.destroy()

                    # Play sound
                    SoundManager.get_soundmanager().play_sound("player_death", False)

                    ScoreManager.reset_score()
                    gui_manager.hide_all_texts()
                    Window.is_in_menu = True
                    menu()

    update_components()


def update_components():
    for entity in Entity.list_entities():
        for component in entity.list_components():
            component.update(entity)


def destroy():
    pass


def game_launch():
    if Window.is_in_menu:
        Window.is_in_menu = False
        frame_count = 0
        launch_time = time.time()

        # Window init
        window = Window.get_window()
        window.apply_color()

        # Game logic init
        init()

        fps = 0
        frame_time = 1 / WindowConfig.TARGET_FPS
        while True:
            start_time = time.time()

            # Game logic update
            update()

            # Render update
            window.update(fps)

            elapsed_time = time.time() - start_time
            if elapsed_time < frame_time:
                # Sleep
                get_now=time.perf_counter
                now = get_now()
                end = now + (frame_time - elapsed_time)
                while now < end:
                    now = get_now()

            frame_count += 1
            if time.time() - launch_time >= 1.0:
                fps = frame_count / (time.time() - launch_time)
                frame_count = 0
                launch_time += 1.0


def menu():
    # Window init
    window.display_window.bgpic("res/menu_bg.gif")

    window.get_window().display_window.onkeypress(game_launch, "Control_L")
    window.get_window().display_window.listen()
    while True:
        window.display_window.update()


def score_management():
    global _last_score_give

    elapsed_time = time.time() - _last_score_give

    if elapsed_time >= 1.0:
        ScoreManager.add_to_score(GameConfig.POINTS_PER_SECOND)
        _last_score_give = time.time()


if __name__ == "__main__":
    menu()
