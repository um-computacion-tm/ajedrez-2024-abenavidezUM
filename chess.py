from board import Board
from moves import PieceError, MoveError, PositionInvalid, MovePieceInvalid, KingError, LocationError, ChessInvalid

class Chess:
    """
    Manages the overall chess game, including moves, turns, and game state.
    """

    def __init__(self):
        """
        Initializes the chess game with a new board and sets the starting turn to 'WHITE'.
        """
        self.board = Board()
        self.turn = "WHITE"

    def move(self, from_input, to_input):
        """
        Processes a move from one position to another.
        """
        x, y = self.translate_input(from_input)
        x1, y1 = self.translate_input(to_input)
        
        piece = self.own_pieces(x, y, from_input)
        destination = (x1, y1)
        
        self.board.move(piece, destination)
        result = self.check_move()
        return result

    def check_move(self):
        """
        Checks the result of a move and updates the game state.
        """
        status = self.check_victory()
        if status == True:
            self.change_turn()
            return True
        else:
            return status

    def change_turn(self):
        """
        Switches the turn to the next player.
        """
        self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"

    def next_turn(self):
        """
        Returns the next player's turn without changing the current turn.
        """
        return "BLACK" if self.turn == "WHITE" else "WHITE"

    def print_board(self):
        """
        Prints the current state of the chess board.
        """
        self.board.print_board()

    def own_pieces(self, x, y, from_input):
        """
        Checks if the piece at the given position belongs to the current player.
        """
        piece = self.board.get_piece(x, y)
        if piece is None:
            raise PieceError(f'En la posición "{from_input}" no hay ninguna pieza.')

        if self.turn.lower() == piece.color:
            return piece
        else:
            raise LocationError("No puedes mover una pieza de un color diferente.")
            
    def translate_input(self, input_str):
        """
        Transforms an input string like 'A2' into board coordinates (row, col).
        """
        if len(input_str) != 2:
            raise ValueError("La entrada debe tener 2 caracteres, como 'A2'.")

        letter_to_col = {
            'A': 0, 'B': 1, 'C': 2, 'D': 3,
            'E': 4, 'F': 5, 'G': 6, 'H': 7
        }

        letter = input_str[0].upper()
        num = input_str[1]
        
        if letter not in letter_to_col:
            raise PositionInvalid(f"El primer carácter '{letter}' debe ser una letra de A a H.")
        col = letter_to_col[letter]

        try:
            row = int(num)
            if row < 1 or row > 8:
                raise PositionInvalid(f"El segundo carácter '{num}' debe ser un número de 1 a 8.")
            row_index = row - 1  # Map rank to row index (1-8 to 0-7)
            return (row_index, col)
        except ValueError:
            raise ValueError(f"El segundo carácter '{num}' debe ser un número.")

    def check_victory(self):
        """
        Checks the current game state to determine if there is a winner or a draw.
        """
        white_pieces, black_pieces = self.board.pieces_on_board()

        if black_pieces == 0:
            return "White wins"
        elif white_pieces == 0:
            return "Black wins"
        elif white_pieces + black_pieces == 2:
            return "Draw"
        return True
