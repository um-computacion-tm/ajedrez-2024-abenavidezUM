from rook import Rook
from knight import Knight
from bishop import Bishop
from pawn import Pawn
from queen import Queen
from king import King
from enums import Player

class game_state:
    # Initialize 2D array to represent the chess board
    def __init__(self):
        # The board is a 2D array
        self.move_log = []
        self.white_turn = True
        self.valid_moves = {}

        self.can_en_passant_bool = False
        self._en_passant_previous = (-1, -1)

        self.checkmate = False
        self.stalemate = False
        self._is_check = False

        # TODO: REMOVE THESE TWO LATER
        self._white_king_location = [0, 3]
        self._black_king_location = [7, 3]

        # Has king not moved, has Rook1(col=0) not moved, has Rook2(col=7) not moved
        self.white_king_can_castle = [True, True, True]  
        self.black_king_can_castle = [True, True, True]

        # Initialize White pieces
        white_rook_1 = Rook('r', 0, 0, Player.PLAYER_1)
        white_rook_2 = Rook('r', 0, 7, Player.PLAYER_1)
        white_knight_1 = Knight('n', 0, 1, Player.PLAYER_1)
        white_knight_2 = Knight('n', 0, 6, Player.PLAYER_1)
        white_bishop_1 = Bishop('b', 0, 2, Player.PLAYER_1)
        white_bishop_2 = Bishop('b', 0, 5, Player.PLAYER_1)
        white_queen = Queen('q', 0, 4, Player.PLAYER_1)
        white_king = King('k', 0, 3, Player.PLAYER_1)
        white_pawn_1 = Pawn('p', 1, 0, Player.PLAYER_1)
        white_pawn_2 = Pawn('p', 1, 1, Player.PLAYER_1)
        white_pawn_3 = Pawn('p', 1, 2, Player.PLAYER_1)
        white_pawn_4 = Pawn('p', 1, 3, Player.PLAYER_1)
        white_pawn_5 = Pawn('p', 1, 4, Player.PLAYER_1)
        white_pawn_6 = Pawn('p', 1, 5, Player.PLAYER_1)
        white_pawn_7 = Pawn('p', 1, 6, Player.PLAYER_1)
        white_pawn_8 = Pawn('p', 1, 7, Player.PLAYER_1)

        # Initialize Black Pieces
        black_rook_1 = Rook('r', 7, 0, Player.PLAYER_2)
        black_rook_2 = Rook('r', 7, 7, Player.PLAYER_2)
        black_knight_1 = Knight('n', 7, 1, Player.PLAYER_2)
        black_knight_2 = Knight('n', 7, 6, Player.PLAYER_2)
        black_bishop_1 = Bishop('b', 7, 2, Player.PLAYER_2)
        black_bishop_2 = Bishop('b', 7, 5, Player.PLAYER_2)
        black_queen = Queen('q', 7, 4, Player.PLAYER_2)
        black_king = King('k', 7, 3, Player.PLAYER_2)
        black_pawn_1 = Pawn('p', 6, 0, Player.PLAYER_2)
        black_pawn_2 = Pawn('p', 6, 1, Player.PLAYER_2)
        black_pawn_3 = Pawn('p', 6, 2, Player.PLAYER_2)
        black_pawn_4 = Pawn('p', 6, 3, Player.PLAYER_2)
        black_pawn_5 = Pawn('p', 6, 4, Player.PLAYER_2)
        black_pawn_6 = Pawn('p', 6, 5, Player.PLAYER_2)
        black_pawn_7 = Pawn('p', 6, 6, Player.PLAYER_2)
        black_pawn_8 = Pawn('p', 6, 7, Player.PLAYER_2)

        self.board = [
            [white_rook_1, white_knight_1, white_bishop_1, white_king, white_queen, white_bishop_2, white_knight_2,
             white_rook_2],
            [white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4, white_pawn_5, white_pawn_6, white_pawn_7,
             white_pawn_8],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4, black_pawn_5, black_pawn_6, black_pawn_7,
             black_pawn_8],
            [black_rook_1, black_knight_1, black_bishop_1, black_king, black_queen, black_bishop_2, black_knight_2,
             black_rook_2]
        ]