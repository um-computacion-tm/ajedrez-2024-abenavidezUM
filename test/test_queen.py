import unittest

from test.test_piece import BaseTestPiece
from queen import Queen

class TestQueen(BaseTestPiece):
    def setUp(self):
        super().setUp()
        self.piece = Queen("white", (4, 4))
        self.positions[4][4] = self.piece
        
        # Movimientos válidos para la reina
        self.valid_moves = [
            (4, 0), (4, 7), (0, 4), (7, 4),
            (0, 0), (7, 7), (0, 7), (7, 0),
            (3, 3), (5, 5), (3, 5), (5, 3)
        ]
        
        # Movimientos inválidos para la reina
        self.invalid_moves = [
            (5, 2), (2, 5), (1, 6)
        ]
        
        # Configuración para pruebas de captura
        self.opponent_piece_type = Queen
        self.opponent_piece_position = (6, 6)
        
        self.friendly_piece_type = Queen
        self.friendly_piece_position = (2, 2)
