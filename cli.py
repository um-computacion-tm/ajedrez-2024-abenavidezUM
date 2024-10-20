from chess import Chess
from moves import PieceError, MoveError, PositionInvalid, MovePieceInvalid, KingError, LocationError, ChessInvalid
import os

class CLI:
    """
    Provides a command-line interface (CLI) for playing a chess game.
    """
    
    def __init__(self):
        """
        Initializes the CLI with a new Chess game instance and game state tracking.
        """
        self.chess_game = Chess()
        self.game_over = False
        self.result = None

    def menu(self):
        """
        Displays the main menu and handles user selection to start or exit the game.
        """
        while True:
            self.display_main_menu()
            selection = input("Type your selection here: ")
            option = self.validate_option("start_game", selection)

            if option == "Invalid option":
                print("\nInvalid option\n")
            elif option == "Game Over":
                print("\nGame Over\n")
                break
            elif option == "Game Started":
                self.start_new_game()
                if self.game_over:
                    break

    def display_main_menu(self):
        print('Select an Option')
        print('1) Start Game')
        print('2) Exit\n')

    def start_new_game(self):
        self.chess_game = Chess()
        self.clear_terminal()
        self.game_over = False
        self.result = None
        self.start_game()

    def validate_option(self, menu_type, option):
        result = ""
        if menu_type == "start_game": 
            if option not in ["1", "2"]:
                result = "Invalid option"
            elif option == "2":
                result = "Game Over"
            elif option == "1":
                result = "Game Started"
        elif menu_type == "continue_game":
            if option not in ["1", "2", "3"]:
                result = "Invalid option"
            elif option == "3":
                result = "Resign"
            elif option == "2":
                result = "Draw"
            elif option == "1":
                result = "Move piece"
        return result

    def start_game(self):
        """
        Starts the game loop, handling player turns until the game ends.
        """
        while not self.game_over:
            if not self.turn_menu():
                break
            self.display_board_and_turn()

            from_input, to_input = self.get_move_input() 
            result = self.attempt_move(from_input, to_input) 

            if result in ["Black wins", "White wins", "Draw"]: 
                print(f'\n{result}')
                print("\nGame Over\n")
                self.game_over = True
                self.result = result
                return True
        return self.game_over

    def display_board_and_turn(self):
        """
        Clears the terminal and displays the current board and whose turn it is.
        """
        self.clear_terminal()
        print(f"\n  {self.chess_game.turn} TO MOVE\n")
        self.chess_game.print_board()

    def get_move_input(self):
        """
        Prompts the player to input their move.
        """
        print('\nEnter your move')
        from_input = input('From: ')
        to_input = input('To: ')
        print('\n')
        return from_input, to_input

    def attempt_move(self, from_input, to_input, test_mode=False):
        result = None
        try:
            self.clear_terminal()
            print('\n')
            result = self.chess_game.move(from_input, to_input)
        except (ValueError, KingError, PieceError, MovePieceInvalid, MoveError, PositionInvalid, LocationError, ChessInvalid) as e:
            if test_mode:
                raise
            print(f"\nError: {e}\n")
        except Exception as e:
            if test_mode:
                raise
            print("\nAn unexpected error occurred.\n")
        finally:
            return result


    def turn_menu(self):
        """
        Displays the menu for the player's turn and handles their selection.
        """
        continue_game = False
        while True:
            self.display_turn_menu()
            try:
                selection = input("\nType your selection here: ") 
            except (EOFError, StopIteration):
                continue_game = False  # Exit the loop if input is exhausted during testing
                break
            option = self.validate_option("continue_game", selection) 

            if option == "Invalid option":
                self.handle_invalid_option(selection) 
            elif option == "Resign":
                self.handle_resignation()
                continue_game = False
                break
            elif option == "Draw": 
                if self.handle_draw():
                    continue_game = False
                    break
                else:
                    continue  # Ask for input again
            elif option == "Move piece": 
                continue_game = True
                break
        return continue_game


    def display_turn_menu(self):
        """
        Displays the options available to the player on their turn.
        """
        print('\n')
        self.chess_game.print_board()
        print('\n')
        print(f"Turn: {self.chess_game.turn}")
        print('\nSelect an Option')
        print('1. Move piece')
        print('2. Draw')
        print('3. Finish')

    def handle_invalid_option(self, selection):
        """
        Handles invalid menu options selected by the user.
        """
        self.clear_terminal()
        print("\n" + f'{selection} is an invalid option, try again' + "\n")

    def handle_resignation(self):
        """
        Handles the player's resignation and declares the winner.
        """
        player = self.chess_game.turn
        print(f"\n{player} resigns the game")
        winner = self.chess_game.next_turn()
        print(f"\n{winner} WINS")
        self.game_over = True
        self.result = f"{winner} WINS"

    def handle_draw(self):
        """
        Handles a draw offer from the player.
        """
        if self.draw(self.chess_game.turn): 
            print("\nGame Drawn")
            self.game_over = True
            self.result = "Game Drawn"
            return True
        else:
            rejecting_player = self.chess_game.next_turn()
            print(f"\n{rejecting_player} REJECTS THE DRAW")
            return False

    def draw(self, player):
        """
        Offers a draw to the opponent and processes their response.
        """
        print(f"\n{player} wants to draw the game")
        print(f"\n{self.chess_game.next_turn()}, Do you want to accept the draw? [Y/N]")
        
        while True:
            try:
                option = input("Type your answer here: ") 
            except (EOFError, StopIteration):
                return False  # Assume draw is declined if input is exhausted

            if option.lower() == "y":
                return True
            elif option.lower() == "n":
                return False
            else:
                print("\nInvalid input. Please enter y or n.")

    def clear_terminal(self):
        """
        Clears the terminal screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    cli = CLI()
    cli.menu()
