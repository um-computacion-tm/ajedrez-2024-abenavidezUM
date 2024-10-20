import unittest


from test.base_test_piece import BaseTestPiece
from bishop import Bishop

class TestBishop(BaseTestPiece, unittest.TestCase):
    def create_piece(self):
        return Bishop("white", (4, 4))

    def setUp(self):
        super().setUp()
        self.valid_moves = [
            (0, 0), (7, 7), (1, 7), (7, 1)
        ]
        self.invalid_moves = [
            (4, 5), (5, 4), (4, 0), (0, 4)
        ]
        self.opponent_piece_type = Bishop
        self.opponent_piece_position = (7, 7)
        self.friendly_piece_type = Bishop
        self.friendly_piece_position = (1, 7)
