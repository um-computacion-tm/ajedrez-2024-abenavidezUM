import unittest
from pawn import Pawn

class TestPawn(unittest.TestCase):
    def setUp(self):
        self.pawn_white = Pawn("white", (6, 4))
        self.pawn_black = Pawn("black", (1, 4))
        self.positions = [[None for _ in range(8)] for _ in range(8)]
        self.positions[6][4] = self.pawn_white
        self.positions[1][4] = self.pawn_black

    def test_white_pawn_initial_double_move(self):
        self.assertTrue(self.pawn_white.check_move(self.positions, (4, 4)))

    def test_black_pawn_initial_double_move(self):
        self.assertTrue(self.pawn_black.check_move(self.positions, (3, 4)))

    def test_pawn_single_move(self):
        self.assertTrue(self.pawn_white.check_move(self.positions, (5, 4)))
        self.assertTrue(self.pawn_black.check_move(self.positions, (2, 4)))

    def test_pawn_invalid_move_forward(self):
        self.assertFalse(self.pawn_white.check_move(self.positions, (7, 4)))
        self.assertFalse(self.pawn_black.check_move(self.positions, (0, 4)))

    def test_pawn_diagonal_capture(self):
        opponent_piece_white = Pawn("black", (5, 3))
        opponent_piece_black = Pawn("white", (2, 3))
        self.positions[5][3] = opponent_piece_white
        self.positions[2][3] = opponent_piece_black
        self.assertTrue(self.pawn_white.check_move(self.positions, (5, 3)))
        self.assertTrue(self.pawn_black.check_move(self.positions, (2, 3)))

    def test_pawn_invalid_diagonal_without_capture(self):
        self.assertFalse(self.pawn_white.check_move(self.positions, (5, 5)))
        self.assertFalse(self.pawn_black.check_move(self.positions, (2, 5)))

    def test_pawn_blocked_forward(self):
        blocking_piece_white = Pawn("black", (5, 4))
        blocking_piece_black = Pawn("white", (2, 4))
        self.positions[5][4] = blocking_piece_white
        self.positions[2][4] = blocking_piece_black
        self.assertFalse(self.pawn_white.check_move(self.positions, (5, 4)))
        self.assertFalse(self.pawn_black.check_move(self.positions, (2, 4)))

if __name__ == '__main__':
    unittest.main()
