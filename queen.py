from piece import Piece

class Queen(Piece):
    """
    Represents a queen chess piece, inheriting from the Piece base class.
    """

    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self):
        return "♕" if self.color == "white" else "♛"

    def check_move(self, positions, new_position):
        destination_piece = positions[new_position[0]][new_position[1]]
        if destination_piece is not None and destination_piece.color == self.color:
            return False
        return (
            self.diagonal_move(positions, new_position) or
            self.horizontal_move(positions, new_position) or
            self.vertical_move(positions, new_position)
        )
