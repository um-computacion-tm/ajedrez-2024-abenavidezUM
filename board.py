from piece import Piece
from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from rook import Rook
from moves import PieceError, MoveError, MovePieceInvalid, KingError

class Board:
    """
    Represents the chess board and manages the state of the game.
    """

    def __init__(self, for_test=False):
        """
        Initializes the chess board with pieces set up in their starting positions,
        unless 'for_test' is True, in which case the board is initialized empty.

        Parameters:
            for_test (bool): If True, the board will be empty for testing purposes.
        """
        self.positions = [[None for _ in range(8)] for _ in range(8)]

        if not for_test:
            self.setup_pieces()
