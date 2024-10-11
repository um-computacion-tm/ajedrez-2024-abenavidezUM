from piece import LinearPiece

class Rook(LinearPiece):
    def __str__(self):
        return "♖" if self.color == "white" else "♜"

    def is_valid_direction(self, new_position):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        # La torre se mueve en línea recta horizontal o vertical
        return new_x == current_x or new_y == current_y
