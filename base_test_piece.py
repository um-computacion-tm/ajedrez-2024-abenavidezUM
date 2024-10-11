from abc import ABC, abstractmethod

class BaseTestPiece(ABC):
    def setUp(self):
        self.positions = [[None for _ in range(8)] for _ in range(8)]
        self.piece = self.create_piece()
        x, y = self.piece.position
        self.positions[x][y] = self.piece

    @abstractmethod
    def create_piece(self):
        """Debe ser implementado por las clases hijas para crear la pieza específica."""
        pass

    def test_valid_moves(self):
        for move in self.valid_moves:
            with self.subTest(move=move):
                self.assertTrue(self.piece.check_move(self.positions, move))

    def test_invalid_moves(self):
        for move in self.invalid_moves:
            with self.subTest(move=move):
                self.assertFalse(self.piece.check_move(self.positions, move))

    def test_capture_opponent_piece(self):
        x, y = self.opponent_piece_position
        opponent_piece = self.opponent_piece_type("black", (x, y))
        self.positions[x][y] = opponent_piece
        self.assertTrue(self.piece.check_move(self.positions, (x, y)))

    def test_blocked_by_friendly_piece(self):
        x, y = self.friendly_piece_position
        friendly_piece = self.friendly_piece_type("white", (x, y))
        self.positions[x][y] = friendly_piece
        self.assertFalse(self.piece.check_move(self.positions, (x, y)))