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

    def get_piece(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        else:
            return None
        
    def is_valid_piece(self, row, col):
        evaluated_piece = self.get_piece(row, col)
        return evaluated_piece is not None and evaluated_piece != Player.EMPTY
    
    def get_valid_moves(self, starting_square):

        '''
        remove pins from valid moves (unless the pinned piece move can get rid of a check and checks is empty
        remove move from valid moves if the move falls within a check piece's valid move
        if the moving piece is a king, the ending square cannot be in a check
        '''

        current_row = starting_square[0]
        current_col = starting_square[1]

        if self.is_valid_piece(current_row, current_col):
            valid_moves = []
            moving_piece = self.get_piece(current_row, current_col)
            if self.get_piece(current_row, current_col).is_player(Player.PLAYER_1):
                king_location = self._white_king_location
            else:
                king_location = self._black_king_location
            group = self.check_for_check(king_location, moving_piece.get_player())
            checking_pieces = group[0]
            pinned_pieces = group[1]
            pinned_checks = group[2]
            initial_valid_piece_moves = moving_piece.get_valid_piece_moves(self)

            # immediate check
            if checking_pieces:
                for move in initial_valid_piece_moves:
                    can_move = True
                    for piece in checking_pieces:
                        if moving_piece.get_name() is "k":
                            temp = self.board[current_row][current_col]
                            self.board[current_row][current_col] = Player.EMPTY
                            temp2 = self.board[move[0]][move[1]]
                            self.board[move[0]][move[1]] = temp
                            if not self.check_for_check(move, moving_piece.get_player())[0]:
                                pass
                            else:
                                can_move = False
                            self.board[current_row][current_col] = temp
                            self.board[move[0]][move[1]] = temp2
                        elif move == piece and len(checking_pieces) == 1 and moving_piece.get_name() is not "k" and \
                                (current_row, current_col) not in pinned_pieces:
                            pass
                        elif move != piece and len(checking_pieces) == 1 and moving_piece.get_name() is not "k" and \
                                (current_row, current_col) not in pinned_pieces:
                            temp = self.board[move[0]][move[1]]
                            self.board[move[0]][move[1]] = moving_piece
                            self.board[current_row][current_col] = Player.EMPTY
                            if self.check_for_check(king_location, moving_piece.get_player())[0]:
                                can_move = False
                            self.board[current_row][current_col] = moving_piece
                            self.board[move[0]][move[1]] = temp
                        else:
                            can_move = False
                    if can_move:
                        valid_moves.append(move)
                self._is_check = True

            # pinned checks
            elif pinned_pieces and moving_piece.get_name() is not "k":
                if starting_square not in pinned_pieces:
                    for move in initial_valid_piece_moves:
                        valid_moves.append(move)
                elif starting_square in pinned_pieces:
                    for move in initial_valid_piece_moves:

                        temp = self.board[move[0]][move[1]]
                        self.board[move[0]][move[1]] = moving_piece
                        self.board[current_row][current_col] = Player.EMPTY
                        if not self.check_for_check(king_location, moving_piece.get_player())[0]:
                            valid_moves.append(move)
                        self.board[current_row][current_col] = moving_piece
                        self.board[move[0]][move[1]] = temp
            else:
                if moving_piece.get_name() is "k":
                    for move in initial_valid_piece_moves:
                        temp = self.board[current_row][current_col]
                        temp2 = self.board[move[0]][move[1]]
                        self.board[current_row][current_col] = Player.EMPTY
                        self.board[move[0]][move[1]] = temp
                        if not self.check_for_check(move, moving_piece.get_player())[0]:
                            valid_moves.append(move)
                        self.board[current_row][current_col] = temp
                        self.board[move[0]][move[1]] = temp2
                else:
                    for move in initial_valid_piece_moves:
                        valid_moves.append(move)

            return valid_moves
        else:
            return None

     # 0 if white lost, 1 if black lost, 2 if stalemate, 3 if not game over

    def checkmate_stalemate_checker(self):
        all_white_moves = self.get_all_legal_moves(Player.PLAYER_1)
        all_black_moves = self.get_all_legal_moves(Player.PLAYER_2)
        if self._is_check and self.whose_turn() and not all_white_moves:
            print("white lost")
            return 0
        elif self._is_check and not self.whose_turn() and not all_black_moves:
            print("black lost")
            return 1
        elif not all_white_moves and not all_black_moves:
            return 2
        else:
            return 3