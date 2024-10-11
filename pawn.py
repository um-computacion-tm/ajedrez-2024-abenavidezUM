from piece import Piece

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self):
        return "♙" if self.color == "white" else "♟"

    def check_move(self, positions, new_position):
        if self.color == "white":
            return self.is_valid_pawn_move(positions, new_position, -1, 6)
        else:
            return self.is_valid_pawn_move(positions, new_position, 1, 1)

    def is_valid_pawn_move(self, positions, new_position, direction, initial_row):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)

        # Movimiento hacia adelante
        if new_y == current_y:
            # Primer movimiento puede ser de dos pasos
            if current_x == initial_row:
                if self.move_one_cell(positions, new_position, direction):
                    return True
                elif (new_x == current_x + 2 * direction and
                      positions[current_x + direction][current_y] is None and
                      positions[new_x][new_y] is None):
                    return True
            # Movimientos posteriores solo pueden ser de un paso
            elif self.move_one_cell(positions, new_position, direction):
                return True
        # Captura diagonal
        elif (new_x == current_x + direction and
              abs(new_y - current_y) == 1 and
              positions[new_x][new_y] is not None and
              positions[new_x][new_y].color != self.color):
            return True
        return False

    def move_one_cell(self, positions, new_position, direction):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        return (new_x == current_x + direction and
                positions[new_x][new_y] is None)
