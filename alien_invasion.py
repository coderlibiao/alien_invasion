import pygame

from settings import Settings
from ship import Ship
import game_function as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个飞船
    ship = Ship(ai_settings, screen)

    # 开始游戏的主循环
    while True:

        # 监听事件
        gf.check_events(ship)
        ship.update()
        # 每次循环都会重绘屏幕
        gf.update_screen(ai_settings, screen, ship)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
