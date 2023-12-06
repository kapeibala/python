# star.py
import pygame
from pygame.sprite import Sprite
import random

class Star(Sprite):
    """表示单个星星的类"""

    def __init__(self, ai_settings, screen):
        """初始化星星并设置起始位置"""
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载星星图像，并设置rect属性
        original_image = pygame.image.load('images/star.png')  # 替换为你的星星图片路径

        # 加载星星图像，并设置rect属性
        self.image = pygame.image.load('images/star.png')  # 替换为你的星星图片路径
        # 缩放星星图像
        self.image = pygame.transform.scale(original_image, (40, 40))  # 替换为适当的宽度和高度
        self.rect = self.image.get_rect()
        # 初始化星星的位置
        self.reset_star()

    def reset_star(self):
        """将星星放到屏幕上随机位置"""
        self.rect.x = random.randint(0, self.ai_settings.screen_width - self.rect.width)
        self.rect.y = random.randint(0, self.ai_settings.screen_height // 2 - self.rect.height)

    def update(self):
        """更新星星的位置，使其下落"""
        self.rect.y += self.ai_settings.star_speed

        # 如果星星到达屏幕底部，重新放置到顶部
        if self.rect.y >= self.ai_settings.screen_height:
            self.reset_star()

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image, self.rect)
