# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外形人的类"""
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.ai