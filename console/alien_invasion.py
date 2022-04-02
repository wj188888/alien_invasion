# -*- coding: utf-8 -*-

import sys
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    pygame.display.set_caption("Alien Invasion")
    # 设置背景色
    bg_color = (230, 230, 230)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标时间
        gf.check_events()
        # 每次循环时都重绘屏幕
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


