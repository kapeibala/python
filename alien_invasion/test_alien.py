import unittest
from unittest.mock import Mock
from alien_invasion import Alien 

class TestAlien(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def test_initialization(self):
        ai_settings = Mock()
        screen = Mock()

        alien = Alien(ai_settings, screen)

        self.assertGreaterEqual(alien.rect.x, 0)
        self.assertLessEqual(alien.rect.x, ai_settings.screen_width - alien.rect.width)
        self.assertEqual(alien.rect.y, alien.rect.height)
        self.assertIsInstance(alien.x, float)

    def test_check_edges(self):
        ai_settings = Mock()
        screen = Mock()

        alien = Alien(ai_settings, screen)

        self.assertFalse(alien.check_edges())

        alien.rect.right = ai_settings.screen_width
        self.assertTrue(alien.check_edges())

        alien.rect.right = ai_settings.screen_width - 1
        self.assertFalse(alien.check_edges())

        alien.rect.left = 0
        self.assertTrue(alien.check_edges())

    def test_update(self):
        ai_settings = Mock()
        screen = Mock()

        alien = Alien(ai_settings, screen)
        alien.rect.x = 50
        alien.ai_settings.alien_speed_factor = 2
        alien.ai_settings.fleet_direction = 1

        alien.update()
        self.assertEqual(alien.rect.x, 50 + 2)

        alien.ai_settings.fleet_direction = -1
        alien.update()
        self.assertEqual(alien.rect.x, (50 + 2) - 2)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
