from test.base_test_piece import TestPiece
from queen import Queen

class TestQueen(TestPiece):
    def create_piece(self):
        return Queen("white", (4, 4))
    
    def setUp(self):
        super().setUp()
        self.valid_moves = [
            # Horizontal and vertical
            (4, 0), (4, 7), (0, 4), (7, 4),
            # Diagonals
            (0, 0), (7, 7), (1, 7), (7, 1)
        ]
        self.invalid_moves = [
            (5, 6), (2, 5), (3, 6)
        ]
        self.opponent_piece_type = Queen
        self.opponent_piece_position = (4, 6)
        self.friendly_piece_type = Queen
        self.friendly_piece_position = (4, 6)
