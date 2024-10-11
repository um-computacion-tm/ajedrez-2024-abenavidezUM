from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self._color = color
        self._position = position

    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self._position

    @abstractmethod
    def check_move(self, positions, new_position):
        pass

    def get_coordinates(self, new_position):
        current_x, current_y = self.position
        new_x, new_y = new_position
        return new_x, new_y, current_x, current_y
