from piece import Piece

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self._initial_row = 1 if self.color == "white" else 6
        self._direction = 1 if self.color == "white" else -1

    def __str__(self):
        return "♙" if self.color == "white" else "♟"

    def check_move(self, positions, new_position):
        return self.is_valid_pawn_move(positions, new_position)

    def is_valid_pawn_move(self, positions, new_position):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        dx = new_x - current_x
        dy = new_y - current_y

        # Movimiento hacia adelante
        if dy == 0:
            if dx == self._direction:
                if positions[new_x][new_y] is None:
                    return True
            elif dx == 2 * self._direction and current_x == self._initial_row:
                intermediate_x = current_x + self._direction
                if positions[intermediate_x][new_y] is None and positions[new_x][new_y] is None:
                    return True
        # Captura diagonal
        elif abs(dy) == 1 and dx == self._direction:
            destination_piece = positions[new_x][new_y]
            if destination_piece is not None and destination_piece.color != self.color:
                return True
        return False
