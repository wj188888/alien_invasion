# -*- coding: utf-8 -*-

import sys
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的便组
    bullets = Group()

    pygame.display.set_caption("Alien Invasion")
    # 设置背景色
    bg_color = (230, 230, 230)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标时间
        gf.check_events(ai_settings, screen, ship, bullets)
        # 每次循环时都重绘屏幕
        ship.update()
        gf.update_bullets(bullets)
        # print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)


if __name__ == '__main__':
    run_game()
