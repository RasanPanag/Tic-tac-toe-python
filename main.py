import random


class Tic_Tac_Toe:
#The __init__ function is called every time an object is created from a class. The __init__ method
#lets the class initialize the object's attributes and serves no other purpose. It is only used within classes
    def __init__(self):
        self.tictacboard = []


# start with a random player
    def get_random(self): # Start with a random player
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.tictacboard[row][col] = player

    def player_win(self, player):
        win = None

        n = len(self.tictacboard)

        # checking rows and n is here number rows provide by user to check
        for i in range(n):
            win = True # intializing the win to true
            for j in range(n):
                if self.tictacboard[i][j] != player:
                    win = False # if not equal than win will change to False
                    break
            if win:
                return win

        # checking columns and n is here number of colums provided by user to see
        for i in range(n):
            win = True # intializing the win to true
            for j in range(n):
                if self.tictacboard[j][i] != player:
                    win = False # if not equal than win will change to False
                    break
            if win:
                return win

        # checking diagonal and see if the diagonals are match
        win = True  # intializing the win to true
        for i in range(n):
            if self.tictacboard[i][i] != player:
                win = False # if not equal than win will change to False
                break
        if win:
            return win # returning the value of win

        win = True
        for i in range(n):
            if self.tictacboard[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.tictacboard:
            for item in row:
                if item == '-':
                    return False
        return True

# filling out the table with X and O
    def board_filled(self):
        for row in self.tictacboard:
            for item in row:
                if item == '-':
                    return False
        return True



# Creating a board
    def create_board(self):
        for i in range(3): #creating three rows
            row = []
            for j in range(3): #creating three range
                row.append('-')
            self.tictacboard.append(row)

    def show_board(self):
        for row in self.tictacboard:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()
            row, col = list(
                map(int, input("Please enter row and column numbers with a space to fix spot: ").split()))
            print()
            # fixing the spot, we are using -1 here because rows and columns have intial value 0 and user is
            # going to use the real number.
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()

# swapping player after each turn
    def swap_player_turn(self, player):
        # Player X if player O has took his turn or Vice-versa
        return 'X' if player == 'O' else 'O'


# starting the game
Tic_Tac_Toe = Tic_Tac_Toe()
Tic_Tac_Toe.start()
