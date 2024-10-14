from piece import LinearPiece

class Bishop(LinearPiece):
    def __str__(self):
        return "♗" if self.color == "white" else "♝"

    def is_valid_direction(self, new_position):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        # El alfil se mueve en diagonal
        return abs(new_x - current_x) == abs(new_y - current_y)
