# coding=utf-8
import json
class GameStats():
    """跟踪游戏统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 让游戏一开始处于非活动状态
        self.game_active = False

        # 任何情况下都不应重置最高得分
        self.high_score = 0

        # 显示等级
        self.level = 1
        self.high_score = 0
        self.load_high_score()

    def load_high_score(self):
        """从文件加载最高分数."""
        try:
            with open('high_score.json', 'r') as file:
                self.high_score = json.load(file)
        except FileNotFoundError:
            pass  # 没有最高分文件，使用默认值（0）

    def save_high_score(self):
        """将最高分保存到文件."""
        with open('high_score.json', 'w') as file:
            json.dump(self.high_score, file)

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_settings.ship_limit
        # 为每次在开始游戏时都重置得分，我们在reset_stats（）而不是__init__中初始化score
        self.score = 0

