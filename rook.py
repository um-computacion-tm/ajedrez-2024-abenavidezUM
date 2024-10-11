from piece import Piece

class Rook(Piece):
    def __str__(self):
        return "♖" if self.color == "white" else "♜"

    def check_move(self, positions, new_position):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)

        if new_x == current_x or new_y == current_y:
            if new_x == current_x:
                direction = 1 if new_y > current_y else -1
                for y in range(current_y + direction, new_y, direction):
                    if positions[new_x][y] is not None:
                        return False
            else:
                direction = 1 if new_x > current_x else -1
                for x in range(current_x + direction, new_x, direction):
                    if positions[x][new_y] is not None:
                        return False
            destination_piece = positions[new_x][new_y]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False
