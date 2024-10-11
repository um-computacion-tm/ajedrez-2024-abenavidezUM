from piece import Piece

class Knight(Piece):
    def __str__(self):
        return "♘" if self.color == "white" else "♞"

    def check_move(self, positions, new_position):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        dx = abs(new_x - current_x)
        dy = abs(new_y - current_y)

        if (dx, dy) in [(2, 1), (1, 2)]:
            destination_piece = positions[new_x][new_y]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False
