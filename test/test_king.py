from test.base_test_piece import TestPiece
from king import King

class TestKing(TestPiece):
    def create_piece(self):
        return King("white", (4, 4))
    
    def setUp(self):
        super().setUp()
        self.valid_moves = [
            (3, 3), (3, 4), (3, 5),
            (4, 3),         (4, 5),
            (5, 3), (5, 4), (5, 5)
        ]
        self.invalid_moves = [
            (2, 4), (4, 2), (6, 4), (4, 6)
        ]
        self.opponent_piece_type = King
        self.opponent_piece_position = (3, 4)
        self.friendly_piece_type = King
        self.friendly_piece_position = (3, 4)
