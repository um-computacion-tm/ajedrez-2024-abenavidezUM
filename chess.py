from board import Board
from moves import PieceError, MoveError, PositionInvalid, MovePieceInvalid, KingError, LocationError, ChessInvalid

class Chess:
    def __init__(self):
        self.board = Board()
        self.turn = "WHITE"

    def move(self, from_input, to_input):
        from_x, from_y = self.translate_input(from_input)
        to_x, to_y = self.translate_input(to_input)
        
        piece = self.own_pieces(from_x, from_y, from_input)
        
        self.board.move(piece, (to_x, to_y))  # Coordenadas directas
        result = self.check_move()
        return result

    def translate_input(self, input_str):
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
            row_index = 8 - row  # Ahora, '1' -> fila 7
            return (row_index, col)
        except ValueError:
            raise ValueError(f"El segundo carácter '{num}' debe ser un número.")

    def own_pieces(self, x, y, from_input):
        piece = self.board.get_piece(x, y)  # Sin invertir
        if piece is None:
            raise PieceError(f'En la posición "{from_input}" no hay ninguna pieza.')

        if self.turn.lower() == piece.color:
            return piece
        else:
            raise LocationError("No puedes mover una pieza de un color diferente.")

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