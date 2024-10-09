import unittest
from unittest.mock import patch
from cli import CLI

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()

    @patch('builtins.input', side_effect=['1', 'E2', 'E4', '2', 'y', '2', ''])
    @patch('os.system')
    def test_draw_offer_accepted(self, mock_os_system, mock_input):
        with patch('cli.CLI.clear_terminal'):
            self.cli.menu()
            # Game should end in a draw
            self.assertTrue(self.cli.game_over)
            self.assertEqual(self.cli.result, "Game Drawn")

    @patch('builtins.input', side_effect=['1', 'E2', 'E5', '3', '2', ''])
    @patch('os.system')
    def test_invalid_move_and_resign(self, mock_os_system, mock_input):
        with patch('cli.CLI.clear_terminal'):
            self.cli.menu()
            # Since the player resigns, the game should end
            self.assertTrue(self.cli.game_over)
            self.assertEqual(self.cli.result, "BLACK WINS")

    @patch('builtins.input', side_effect=['1', 'E2', 'E4', '2', 'n', '3', '2', ''])
    @patch('os.system')
    def test_start_game(self, mock_os_system, mock_input):
        with patch('cli.CLI.clear_terminal'):
            self.cli.menu()
            # After declining the draw, the game continues
            self.assertFalse(self.cli.game_over)
            self.assertEqual(self.cli.chess_game.turn, "BLACK")

    @patch('builtins.input', side_effect=['2', ''])
    def test_exit_game(self, mock_input):
        with patch('cli.CLI.clear_terminal'):
            self.cli.menu()
            # Game didn't start

if __name__ == '__main__':
    unittest.main()
