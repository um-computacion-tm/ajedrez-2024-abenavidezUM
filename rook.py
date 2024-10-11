from piece import Piece

class Rook(Piece):
    def __str__(self):
        return "♖" if self.color == "white" else "♜"

    def check_move(self, positions, new_position):
        if not self.is_valid_direction(new_position):
            return False

        if not self.is_path_clear(positions, new_position):
            return False

        return self.is_destination_valid(positions, new_position)

    def is_valid_direction(self, new_position):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        # Movimiento válido si es en la misma fila o columna
        return new_x == current_x or new_y == current_y

    def is_path_clear(self, positions, new_position):
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        x_direction = self.get_direction(current_x, new_x)
        y_direction = self.get_direction(current_y, new_y)

        x, y = current_x + x_direction, current_y + y_direction

        while (x, y) != (new_x, new_y):
            if positions[x][y] is not None:
                return False
            x += x_direction
            y += y_direction
        return True

    def get_direction(self, current, new):
        if new > current:
            return 1
        elif new < current:
            return -1
        else:
            return 0
