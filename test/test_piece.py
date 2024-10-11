import unittest

class TestPiece(unittest.TestCase):
    __test__ = False  # Evita que unittest ejecute esta clase

    def setUp(self):
        self.piece = None  # Será definido en las clases hijas
        self.positions = [[None for _ in range(8)] for _ in range(8)]
    
    def test_valid_moves(self):
        for move in self.valid_moves:
            with self.subTest(move=move):
                self.assertTrue(self.piece.check_move(self.positions, move))
    
    def test_invalid_moves(self):
        for move in self.invalid_moves:
            with self.subTest(move=move):
                self.assertFalse(self.piece.check_move(self.positions, move))
    
    def test_capture_opponent_piece(self):
        opponent_piece = self.create_opponent_piece(self.opponent_piece_type, self.opponent_piece_position)
        self.positions[self.opponent_piece_position[0]][self.opponent_piece_position[1]] = opponent_piece
        self.assertTrue(self.piece.check_move(self.positions, self.opponent_piece_position))
    
    def test_blocked_by_friendly_piece(self):
        friendly_piece = self.create_friendly_piece(self.friendly_piece_type, self.friendly_piece_position)
        self.positions[self.friendly_piece_position[0]][self.friendly_piece_position[1]] = friendly_piece
        self.assertFalse(self.piece.check_move(self.positions, self.friendly_piece_position))
    
    # Métodos auxiliares para crear piezas
    def create_opponent_piece(self, piece_class, position):
        return piece_class("black", position)
    
    def create_friendly_piece(self, piece_class, position):
        return piece_class("white", position)
