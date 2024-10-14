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
