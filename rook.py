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
        if new_x == current_x:
            # Movimiento vertical
            direction = 1 if new_y > current_y else -1
            for y in range(current_y + direction, new_y, direction):
                if positions[new_x][y] is not None:
                    return False
        else:
            # Movimiento horizontal
            direction = 1 if new_x > current_x else -1
            for x in range(current_x + direction, new_x, direction):
                if positions[x][new_y] is not None:
                    return False
        return True

    def is_destination_valid(self, positions, new_position):
        new_x, new_y = new_position
        destination_piece = positions[new_x][new_y]
        # El destino es válido si está vacío o tiene una pieza oponente
        return destination_piece is None or destination_piece.color != self.color
