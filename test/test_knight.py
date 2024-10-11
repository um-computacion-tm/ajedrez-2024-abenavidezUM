from base_test_piece import BaseTestPiece
from knight import Knight

class TestKnight(BaseTestPiece):
    def create_piece(self):
        return Knight("white", (4, 4))
    
    def setUp(self):
        super().setUp()
        self.valid_moves = [
            (6, 5), (6, 3), (2, 5), (2, 3),
            (5, 6), (5, 2), (3, 6), (3, 2)
        ]
        self.invalid_moves = [
            (4, 5), (5, 5), (4, 2), (2, 4)
        ]
        self.opponent_piece_type = Knight
        self.opponent_piece_position = (6, 5)
        self.friendly_piece_type = Knight
        self.friendly_piece_position = (6, 5)
