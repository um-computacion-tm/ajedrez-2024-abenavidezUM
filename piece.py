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
        """
        Gets the current position of the piece.
        """
        return self._position

    @position.setter
    def position(self, new_position):
        """
        Sets the position of the piece.
        """
        self._position = new_position

    def __str__(self):
        """
        Returns a string representation of the piece.
        """
        return "?"

    @abstractmethod
    def check_move(self, positions, new_position):
        """
        Abstract method to check if a move is valid for the piece.
        """
        pass

    def get_coordinates(self, new_position):
        """
        Returns the coordinates for the current and new positions.
        """
        new_x, new_y = new_position
        current_x, current_y = self._position
        return new_x, new_y, current_x, current_y

    def diagonal_move(self, positions, new_position):
        """
        Checks if the move is a valid diagonal move, ensuring the path is unobstructed.
        """
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        x_diff, y_diff = new_x - current_x, new_y - current_y

        if abs(x_diff) == abs(y_diff):
            step_x = 1 if x_diff > 0 else -1
            step_y = 1 if y_diff > 0 else -1
            for i in range(1, abs(x_diff)):
                x = current_x + i * step_x
                y = current_y + i * step_y
                if not self.is_in_bounds(x, y):
                    return False
                if positions[x][y] is not None:
                    return False
            return True
        return False

    def horizontal_move(self, positions, new_position):
        """
        Checks if the move is a valid horizontal move, ensuring the path is unobstructed.
        """
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)

        if new_x == current_x and new_y != current_y:
            step = 1 if new_y > current_y else -1
            for i in range(1, abs(new_y - current_y)):
                y = current_y + i * step
                if not self.is_in_bounds(new_x, y):
                    return False
                if positions[new_x][y] is not None:
                    return False
            return True
        return False

    def vertical_move(self, positions, new_position):
        """
        Checks if the move is a valid vertical move, ensuring the path is unobstructed.
        """
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)

        if new_x != current_x and new_y == current_y:
            step = 1 if new_x > current_x else -1
            for i in range(1, abs(new_x - current_x)):
                x = current_x + i * step
                if not self.is_in_bounds(x, new_y):
                    return False
                if positions[x][new_y] is not None:
                    return False
            return True
        return False

    def is_in_bounds(self, x, y):
        """
        Checks if the given coordinates are within the board boundaries.
        """
        return 0 <= x < 8 and 0 <= y < 8
