import unittest
import pygame
from alien_invasion import Ship  

class ShipTestCase(unittest.TestCase):

    def setUp(self):
        """在每个测试方法运行之前都创建一个飞船实例"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.ai_settings = AI_Settings()  # 假设有一个AI_Settings类来初始化游戏设置
        self.ship = Ship(self.ai_settings, self.screen)

    def test_ship_initialization(self):
        """测试飞船是否正确初始化"""
        self.assertEqual(self.ship.rect.centerx, self.ai_settings.screen_width // 2)
        self.assertEqual(self.ship.rect.bottom, self.ai_settings.screen_height)

    def test_ship_update_movement(self):
        """测试飞船的移动更新是否正常"""
        initial_center = self.ship.center

        # 模拟向右移动
        self.ship.moving_right = True
        self.ship.update()
        self.assertEqual(self.ship.center, initial_center + self.ai_settings.ship_speed_factor)

        # 模拟向左移动
        self.ship.moving_left = True
        self.ship.update()
        self.assertEqual(self.ship.center, initial_center)

    def test_ship_update_vertical_movement(self):
        """测试飞船的垂直移动更新是否正常"""
        initial_y = self.ship.rect.y

        # 模拟向上移动
        self.ship.moving_up = True
        self.ship.update()
        self.assertEqual(self.ship.rect.y, initial_y - self.ai_settings.ship_speed_factor)

        # 模拟向下移动
        self.ship.moving_down = True
        self.ship.update()
        self.assertEqual(self.ship.rect.y, initial_y)

    def tearDown(self):
        """在每个测试方法运行之后都关闭游戏窗口"""
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
