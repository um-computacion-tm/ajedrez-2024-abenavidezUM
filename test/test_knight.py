import unittest


from test.base_test_piece import BaseTestPiece
from knight import Knight

class TestKnight(BaseTestPiece, unittest.TestCase):
    def create_piece(self):
        return Knight("white", (4, 4))

    def setUp(self):
        super().setUp()
        self.valid_moves = [
            (2, 3), (2, 5), (3, 2), (3, 6),
            (5, 2), (5, 6), (6, 3), (6, 5)
        ]
        self.invalid_moves = [
            (4, 5), (5, 4), (4, 3), (3, 4)
        ]
        self.opponent_piece_type = Knight
        self.opponent_piece_position = (2, 3)
        self.friendly_piece_type = Knight
        self.friendly_piece_position = (2, 5)
