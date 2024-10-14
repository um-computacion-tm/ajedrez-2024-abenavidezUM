from piece import Piece

class Knight(Piece):
    def __str__(self):
        return "♘" if self.color == "white" else "♞"

    def check_move(self, positions, new_position):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        dx = abs(new_x - current_x)
        dy = abs(new_y - current_y)

        # Verifica si el movimiento es en forma de "L"
        if (dx, dy) not in [(2, 1), (1, 2)]:
            return False

        # Verifica si la casilla de destino es válida (vacía o contiene una pieza oponente)
        if not self.is_destination_valid(positions, new_position):
            return False

        return True
