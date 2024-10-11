from test.base_test_piece import TestPiece
from rook import Rook

class TestRook(TestPiece):
    def create_piece(self):
        return Rook("white", (4, 4))
    
    def setUp(self):
        super().setUp()
        self.valid_moves = [
            (4, 0), (4, 7), (0, 4), (7, 4)
        ]
        self.invalid_moves = [
            (5, 5), (3, 3), (2, 6)
        ]
        self.opponent_piece_type = Rook
        self.opponent_piece_position = (4, 7)
        self.friendly_piece_type = Rook
        self.friendly_piece_position = (4, 7)
