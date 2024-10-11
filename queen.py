from piece import Piece

class Queen(Piece):
    """
    Represents a queen chess piece, inheriting from the Piece base class.
    """

    def __init__(self, color, position):
        """
        Initializes a Queen instance with a color and position.

        Parameters:
            color (str): The color of the queen, e.g., "white" or "black".
            position (tuple): The current position of the queen on the board.
        """
        super().__init__(color, position)

    def __str__(self):
        """
        Returns the Unicode character representing the queen, depending on its color.

        Returns:
            str: "♕" if the queen is white, "♛" if the queen is black.
        """
        return "♕" if self.__color__ == "white" else "♛"

    def check_move(self, positions, new_position):
        """
        Checks if moving to new_position is a valid move for the queen.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        destination_piece = positions[new_position[0]][new_position[1]]
        if destination_piece is not None and destination_piece.__color__ == self.__color__:
            return False
        return (
            self.diagonal_move(positions, new_position) or
            self.horizontal_move(positions, new_position) or
            self.vertical_move(positions, new_position)
        )

    def diagonal_move(self, positions, new_position):
        """
        Checks if the move to new_position is a valid diagonal move.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if it's a valid diagonal move, False otherwise.
        """
        row_diff = new_position[0] - self.position[0]
        col_diff = new_position[1] - self.position[1]
        if abs(row_diff) != abs(col_diff):
            return False

        row_step = 1 if row_diff > 0 else -1
        col_step = 1 if col_diff > 0 else -1

        for i in range(1, abs(row_diff)):
            row = self.position[0] + i * row_step
            col = self.position[1] + i * col_step
            if positions[row][col] is not None:
                return False
        return True

    def horizontal_move(self, positions, new_position):
        """
        Checks if the move to new_position is a valid horizontal move.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if it's a valid horizontal move, False otherwise.
        """
        if self.position[0] != new_position[0]:
            return False

        col_step = 1 if new_position[1] > self.position[1] else -1

        for col in range(self.position[1] + col_step, new_position[1], col_step):
            if positions[self.position[0]][col] is not None:
                return False
        return True

    def vertical_move(self, positions, new_position):
        """
        Checks if the move to new_position is a valid vertical move.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if it's a valid vertical move, False otherwise.
        """
        if self.position[1] != new_position[1]:
            return False

        row_step = 1 if new_position[0] > self.position[0] else -1

        for row in range(self.position[0] + row_step, new_position[0], row_step):
            if positions[row][self.position[1]] is not None:
                return False
        return True
