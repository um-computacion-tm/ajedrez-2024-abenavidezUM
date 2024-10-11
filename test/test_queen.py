import unittest

from test.base_test_piece import BaseTestPiece
from queen import Queen

class TestQueen(BaseTestPiece, unittest.TestCase):
    def create_piece(self):
        return Queen("white", (4, 4))

    def setUp(self):
        super().setUp()
        self.valid_moves = [
            (4, 0), (4, 7), (0, 4), (7, 4),
            (0, 0), (7, 7), (1, 7), (7, 1)
        ]
        self.invalid_moves = [
            (5, 2), (2, 5), (3, 2), (2, 3)
        ]
        self.opponent_piece_type = Queen
        self.opponent_piece_position = (7, 4)
        self.friendly_piece_type = Queen
        self.friendly_piece_position = (4, 7)
