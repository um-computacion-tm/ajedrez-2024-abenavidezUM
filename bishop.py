from piece import Piece

class Bishop(Piece):
    def __str__(self):
        return "♗" if self.color == "white" else "♝"

    def check_move(self, positions, new_position):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)

        if abs(new_x - current_x) == abs(new_y - current_y):
            x_direction = 1 if new_x > current_x else -1
            y_direction = 1 if new_y > current_y else -1
            x, y = current_x + x_direction, current_y + y_direction

            while (x, y) != (new_x, new_y):
                if positions[x][y] is not None:
                    return False
                x += x_direction
                y += y_direction

            destination_piece = positions[new_x][new_y]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False
