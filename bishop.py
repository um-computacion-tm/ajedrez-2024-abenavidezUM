from piece import LinearPiece

class Bishop(LinearPiece):
    def __str__(self):
        return "♗" if self.color == "white" else "♝"

    def is_valid_direction(self, new_position):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        # El alfil se mueve en diagonal
        return abs(new_x - current_x) == abs(new_y - current_y)

    def check_move(self, positions, new_position):
        # Verifica si la dirección del movimiento es válida (diagonal)
        if not self.is_valid_direction(new_position):
            return False

        # Verifica si el camino está libre
        if not self.is_path_clear(positions, new_position):
            return False

        # Verifica si la casilla de destino es válida (vacía o contiene una pieza oponente)
        if not self.is_destination_valid(positions, new_position):
            return False

        return True
