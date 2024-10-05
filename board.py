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

    def setup_pieces(self):
        """
        Sets up all the chess pieces on the board in their initial positions.
        """
        # Black pieces
        self.positions[0][0] = Rook("black", (0, 0))
        self.positions[0][1] = Knight("black", (0, 1))
        self.positions[0][2] = Bishop("black", (0, 2))
        self.positions[0][3] = Queen("black", (0, 3))
        self.positions[0][4] = King("black", (0, 4))
        self.positions[0][5] = Bishop("black", (0, 5))
        self.positions[0][6] = Knight("black", (0, 6))
        self.positions[0][7] = Rook("black", (0, 7))

        for i in range(8):
            self.positions[1][i] = Pawn("black", (1, i))
            self.positions[6][i] = Pawn("white", (6, i))

        # White pieces
        self.positions[7][0] = Rook("white", (7, 0))
        self.positions[7][1] = Knight("white", (7, 1))
        self.positions[7][2] = Bishop("white", (7, 2))
        self.positions[7][3] = Queen("white", (7, 3))
        self.positions[7][4] = King("white", (7, 4))
        self.positions[7][5] = Bishop("white", (7, 5))
        self.positions[7][6] = Knight("white", (7, 6))
        self.positions[7][7] = Rook("white", (7, 7))