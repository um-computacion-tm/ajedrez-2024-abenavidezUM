class ChessInvalid(Exception):
    """
    Base class for chess-related exceptions.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message="An error occurred in the chess game."):
        """
        Initializes the ChessInvalid exception with an optional message.

        Parameters:
            message (str): An explanation of the error.
        """
        super().__init__(message)
