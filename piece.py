from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self._color = color
        self._position = position

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @abstractmethod
    def check_move(self, positions, new_position):
        pass

    def get_coordinates(self, new_position):
        current_x, current_y = self.position
        new_x, new_y = new_position
        return new_x, new_y, current_x, current_y

    def is_destination_valid(self, positions, new_position):
        new_x, new_y = new_position
        if not (0 <= new_x < 8 and 0 <= new_y < 8):
            return False  # La posición está fuera del tablero
        destination_piece = positions[new_x][new_y]
        # El destino es válido si está vacío o tiene una pieza oponente
        return destination_piece is None or destination_piece.color != self.color

# Agregamos la clase LinearPiece aquí
class LinearPiece(Piece):
    def check_move(self, positions, new_position):
        if not self.is_valid_direction(new_position):
            return False

        if not self.is_path_clear(positions, new_position):
            return False

        return self.is_destination_valid(positions, new_position)

    @abstractmethod
    def is_valid_direction(self, new_position):
        pass  # Cada pieza lineal implementará su propia lógica

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
