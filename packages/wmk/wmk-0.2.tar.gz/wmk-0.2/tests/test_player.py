import unittest
import numpy as np
import pyglet
from unittest.mock import Mock, patch
from wmk.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.mock_frame = np.zeros((100, 100, 3), dtype=np.uint8)
        self.frame_generator = Mock(return_value=self.mock_frame)
        self.player = Player(800, 600, self.frame_generator)

    def test_player_initialization(self):
        self.assertEqual(self.player.width, 800)
        self.assertEqual(self.player.height, 600)
        self.assertEqual(self.player.fps, 30)
        self.assertEqual(self.player.mouse_sensitivity, 1)
        self.assertEqual(self.player.keyboard_state, {})
        self.assertEqual(self.player.mouse_state, {})

    def test_key_events(self):
        self.player.on_key_press(pyglet.window.key.A, None)
        self.assertTrue(self.player.keyboard_state[pyglet.window.key.A])
        
        self.player.on_key_release(pyglet.window.key.A, None)
        self.assertFalse(self.player.keyboard_state[pyglet.window.key.A])

    def test_mouse_events(self):
        # Test mouse press
        self.player.on_mouse_press(0, 0, pyglet.window.mouse.LEFT, None)
        self.assertTrue(self.player.mouse_state["LEFT_CLICK"])

        # Test mouse release
        self.player.on_mouse_release(0, 0, pyglet.window.mouse.LEFT, None)
        self.assertFalse(self.player.mouse_state["LEFT_CLICK"])

        # Test mouse motion
        self.player.on_mouse_motion(100, 100, 5, 10)
        self.assertEqual(self.player.mouse_state["MOVE_X"], 5)
        self.assertEqual(self.player.mouse_state["MOVE_Y"], 10)

    @patch('pyglet.sprite.Sprite')
    def test_render_frame(self, mock_sprite):
        self.player.render_frame(self.mock_frame)
        self.assertIsNotNone(self.player.sprite)

    def test_update(self):
        self.player.update(1/30)
        self.frame_generator.assert_called_once_with(
            self.player.keyboard_state, 
            self.player.mouse_state
        )

    def tearDown(self):
        self.player.close()

if __name__ == '__main__':
    unittest.main()
