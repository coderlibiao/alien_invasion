import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_function as gf
from alien import Alien
from game_stats import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)
    # 创建一个飞船
    ship = Ship(ai_settings, screen)

    bullets = Group()

    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环
    while True:

        # 监听事件
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 每次循环都会重绘屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
