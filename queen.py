from piece import LinearPiece

class Queen(LinearPiece):
    def __str__(self):
        return "♕" if self.color == "white" else "♛"

    def is_valid_direction(self, new_position):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        dx = abs(new_x - current_x)
        dy = abs(new_y - current_y)
        # La reina combina los movimientos de la torre y el alfil
        return dx == dy or new_x == current_x or new_y == current_y
