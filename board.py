from piece import Piece
from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from rook import Rook
from moves import PieceError, MoveError, MovePieceInvalid, KingError

class Board:
    def __init__(self, for_test=False):
        self.positions = [[None for _ in range(8)] for _ in range(8)]
        if not for_test:
            self.setup_pieces()

    def setup_pieces(self):
        # Asigna piezas negras a filas 0 y 1
        self.setup_major_pieces('black', 0)
        self.setup_pawns('black', 1)
        # Asigna piezas blancas a filas 6 y 7
        self.setup_pawns('white', 6)
        self.setup_major_pieces('white', 7)

    def setup_major_pieces(self, color, row):
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece_class in enumerate(pieces):
            self.positions[row][col] = piece_class(color, (row, col))

    def setup_pawns(self, color, row):
        for col in range(8):
            self.positions[row][col] = Pawn(color, (row, col))

    def get_piece(self, row, col):
        return self.positions[row][col]
    
    def set_piece_on_board(self, row, col, piece):
        self.positions[row][col] = piece

    def find_piece(self, piece):
        for row in range(8):
            for col in range(8):
                if self.positions[row][col] == piece:
                    return (row, col)
        return None

    def move(self, piece, destination):
        self.validate_move(piece, destination)
        self.execute_move(piece, destination)
        return True

    def validate_move(self, piece, destination):
        current_position = self.find_piece(piece)
        if current_position is None:
            raise PieceError("Piece not found on the board.")

        if not piece.check_move(self.positions, destination):
            raise MovePieceInvalid("Invalid piece movement.")

        dest_piece = self.get_piece(*destination)
        if dest_piece is not None:
            if dest_piece.color == piece.color:
                raise MoveError("You cannot move to a square occupied by your own piece.")
            if isinstance(dest_piece, King):
                raise KingError("You cannot capture the opponent's king.")

    def execute_move(self, piece, destination):
        current_row, current_col = self.find_piece(piece)
        dest_row, dest_col = destination
        captured_piece = self.get_piece(dest_row, dest_col)

        from_square = self.coords_to_notation(current_row, current_col)
        to_square = self.coords_to_notation(dest_row, dest_col)
        print(f'Moviendo {piece} de {from_square} a {to_square}')  # Mensaje en notación de ajedrez

        self.set_piece_on_board(dest_row, dest_col, piece)
        self.set_piece_on_board(current_row, current_col, None)
        piece.position = (dest_row, dest_col)

        if captured_piece is not None:
            captured_piece.position = None  # Eliminar la pieza capturada del tablero
            print(f'Capturado: {captured_piece}')  # Depuración

    def print_board(self):
        print("    A  B  C  D  E  F  G  H")
        print("   ------------------------")
        for row in range(8):
            line = f'{8-row} |'
            for col in range(8):
                piece = self.get_piece(row, col)
                line += f' {str(piece) if piece else "."} '
            line += f'| {8-row}'
            print(line)
        print("   ------------------------")
        print("    A  B  C  D  E  F  G  H")

    def pieces_on_board(self):
        white_pieces = 0
        black_pieces = 0
        for row in self.positions:
            for piece in row:
                if piece:
                    if piece.color == "white":
                        white_pieces += 1
                    else:
                        black_pieces += 1
        return (white_pieces, black_pieces)
    
    def color_pieces(self, x, y):
        piece = self.get_piece(x, y)
        if piece is None:
            raise PieceError("Piece not found on the board.")
        else:
            return piece.color
        
    def clean_board(self):
        self.positions = [[None for _ in range(8)] for _ in range(8)]

    def coords_to_notation(self, row, col):
        """
        Convierte coordenadas de la matriz a notación de ajedrez (e.g., (6,4) -> 'e2')
        """
        file = chr(ord('A') + col)
        rank = 8 - row
        return f"{file}{rank}"