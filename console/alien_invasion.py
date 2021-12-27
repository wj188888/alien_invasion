import sys
import pygame

from setting import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # 定义一个屏幕背景板
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # 将游戏在全屏模式下运行
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # 设置背景色
        # self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    # 这是一个辅助函数
    def _check_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 针对键盘时间按下和弹起做判断
            elif event.type == pygame.KEYDOWN:
                # 在下方定义了辅助函数，这个是按下键盘
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # 弹起键盘
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''响应按键'''
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船,标记飞船向右移动
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船,标记飞船向左移动
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # 如果键盘监听到用户的q键，就退出游戏
            sys.exit()

    def _check_keyup_events(self, event):
        '''响应松开'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False



    def _update_screen(self):
        '''更新屏幕上的图像， 并切换到新屏幕上'''
        # 每次循环时都重绘屏幕,给与颜色
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()