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
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)

        # Verifica si el movimiento es adyacente (máximo 1 casilla en cualquier dirección)
        if abs(new_x - current_x) <= 1 and abs(new_y - current_y) <= 1:
            # Utiliza el método auxiliar para validar la casilla de destino
            if self.is_destination_valid(positions, new_position):
                return True
        return False
