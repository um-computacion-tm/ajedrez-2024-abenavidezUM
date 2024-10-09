import unittest
from board import Board
from king import King
from queen import Queen
from rook import Rook
from moves import PieceError, MovePieceInvalid, MoveError, KingError

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_king = self.board.get_piece(7, 4)
        self.black_king = self.board.get_piece(0, 4)

    def test_initial_setup(self):
        # Ensure that kings are in their correct starting positions
        self.assertIsInstance(self.white_king, King)
        self.assertEqual(self.white_king.color, "white")
        self.assertIsInstance(self.black_king, King)
        self.assertEqual(self.black_king.color, "black")

    def test_move_piece(self):
        # Move a pawn forward
        pawn = self.board.get_piece(6, 4)
        self.board.move(pawn, (4, 4))
        self.assertIs(self.board.get_piece(4, 4), pawn)
        self.assertIsNone(self.board.get_piece(6, 4))
        self.assertEqual(pawn.position, (4, 4))

    def test_move_invalid(self):
        # Attempt an invalid move
        pawn = self.board.get_piece(6, 4)
        with self.assertRaises(MovePieceInvalid):
            self.board.move(pawn, (3, 4))

    def test_capture_opponent_piece(self):
        # Move white pawn to capture black pawn
        white_pawn = self.board.get_piece(6, 0)
        self.board.move(white_pawn, (4, 0))
        black_pawn = self.board.get_piece(1, 1)
        self.board.move(black_pawn, (3, 1))
        self.board.move(white_pawn, (3, 1))
        self.assertIs(self.board.get_piece(3, 1), white_pawn)
        self.assertIsNone(self.board.get_piece(1, 1))
        self.assertEqual(white_pawn.position, (3, 1))

    def test_capture_own_piece(self):
        # Attempt to capture own piece
        pawn = self.board.get_piece(6, 0)
        with self.assertRaises(MoveError):
            self.board.move(pawn, (7, 0))

    def test_capture_king(self):
        # Adjusted test to attempt a valid move that tries to capture the opponent's king
        queen = self.board.get_piece(7, 3)  # White queen at (7, 3)
        # Clear the path for the queen to move vertically to (0, 3)
        for i in range(1, 7):
            self.board.set_piece_on_board(7 - i, 3, None)
        # Move queen to (1, 3) first
        self.board.move(queen, (1, 3))
        # Attempt to capture the black king at (0, 4) from (1, 3)
        # Clear the path diagonally
        self.board.set_piece_on_board(0, 4, self.black_king)  # Ensure black king is at (0, 4)
        with self.assertRaises(KingError):
            self.board.move(queen, (0, 4))

    def test_blocked_by_friendly_piece_at_destination(self):
        # Place a friendly piece at the destination
        friendly_piece = Queen("white", (4, 6))
        self.board.set_piece_on_board(4, 6, friendly_piece)
        queen = self.board.get_piece(7, 3)
        with self.assertRaises(MoveError):
            self.board.move(queen, (4, 6))

if __name__ == '__main__':
    unittest.main()
