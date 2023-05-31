import pygame

from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个飞船
    ship = Ship(ai_settings, screen)

    bullets = Group()
    # 开始游戏的主循环
    while True:

        # 监听事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        print(len(bullets))
        # 每次循环都会重绘屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
