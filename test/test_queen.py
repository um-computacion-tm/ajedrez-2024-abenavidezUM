from test_piece import TestPiece
from queen import Queen

class TestQueen(TestPiece):
    def setUp(self):
        super().setUp()
        self.piece = Queen("white", (4, 4))
        self.positions[4][4] = self.piece
        
        # Movimientos válidos para la reina
        self.valid_moves = [
            # Añadir movimientos válidos específicos para la reina
            (4, 0), (4, 7), (0, 4), (7, 4),
            (0, 0), (7, 7), (0, 7), (7, 0),
            (3, 4), (4, 3), (5, 4), (4, 5)
        ]
        
        # Movimientos inválidos para la reina
        self.invalid_moves = [
            (5, 2), (2, 5), (3, 6)
        ]
        
        # Configuración para pruebas de captura
        self.opponent_piece_type = Queen
        self.opponent_piece_position = (6, 6)
        
        self.friendly_piece_type = Queen
        self.friendly_piece_position = (2, 2)
