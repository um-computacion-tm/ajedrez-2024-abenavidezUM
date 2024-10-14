from piece import Piece

class King(Piece):
    """
    Represents a king chess piece, inheriting from the Piece base class.
    """

    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self):
        return "♔" if self.color == "white" else "♚"

    def check_move(self, positions, new_position):
        # Verifica si el movimiento es adyacente (máximo 1 casilla en cualquier dirección)
        if not self.is_adjacent_move(new_position, max_distance=1):
            return False

        # Verifica si la casilla de destino es válida (vacía o contiene una pieza oponente)
        if not self.is_destination_valid(positions, new_position):
            return False

        return True
