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

        if abs(new_x - current_x) <= 1 and abs(new_y - current_y) <= 1:
            destination_piece = positions[new_x][new_y]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False
