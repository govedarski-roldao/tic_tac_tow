import os

class GameBoard:
    def __init__(self):
        self.plays = []
        self.p_one = " X "
        self.p_two = " O "
        self.board = {
            'a1': '   ', 'a2': '   ', 'a3': '   ',
            'b1': '   ', 'b2': '   ', 'b3': '   ',
            'c1': '   ', 'c2': '   ', 'c3': '   ',
        }



    def bet(self, player):
        player_column = input(f"Player {player}, which is the column? A, B, C?")
        player_line = input("And what is the line?1, 2 or 3?")
        play_accepted = self.verify_choice(player_column, player_line)
        if play_accepted:
            self.place_play(player, player_column, player_line)
            return False
            self.print_board()
        else:
            return True

    def verify_choice(self, column, line):
        position = f"{column.lower()}{line}"
        if position not in self.board:
            print("Please select a correct value")
            return False
        elif position in self.plays:
            print("Place already occupied, please select other")
            return False
        else:
            self.plays.append(position)
            return True

    def print_board(self):
        os.system('cls')
        print("    A  B   C")
        print(f"1 {self.board['a1']}|{self.board['a2']}|{self.board['a3']}")
        print("------------")
        print(f"2 {self.board['b1']}|{self.board['b2']}|{self.board['b3']}")
        print("------------")
        print(f"3 {self.board['c1']}|{self.board['c2']}|{self.board['c3']}")

    def place_play(self, player, column, line):
        position = f"{column.lower()}{line}"
        if player == 1:
            self.board[position] = self.p_one
        else:
            self.board[position] = self.p_two

    def verify_player(self, symbol):
        if symbol == " X ":
            return [True, "End of the game, player One won this match"]
        else:
            return [True, "End of the game, player Two won this match"]

    def verify_game(self):
        if self.board["a1"] == self.board["a2"] == self.board["a3"] and self.board["a1"] != '   ':
            return self.verify_player(self.board["a1"])
        elif self.board["b1"] == self.board["b2"] == self.board["b3"] and self.board["b1"] != '   ':
            return self.verify_player(self.board["b1"])
        elif self.board["c1"] == self.board["c2"] == self.board["c3"] and self.board["c1"] != '   ':
            return self.verify_player(self.board["c1"])

        elif self.board["a1"] == self.board["b1"] == self.board["c3"] and self.board["a1"] != '   ':
            return self.verify_player(self.board["a1"])
        elif self.board["a2"] == self.board["b2"] == self.board["c2"] and self.board["a2"] != '   ':
            return self.verify_player(self.board["a2"])
        elif self.board["a3"] == self.board["b3"] == self.board["c3"] and self.board["a3"] != '   ':
            return self.verify_player(self.board["a3"])

        elif self.board["a1"] == self.board["b2"] == self.board["c3"] and self.board["a1"] != '   ':
            return self.verify_player(self.board["a1"])
        elif self.board["a3"] == self.board["b2"] == self.board["c1"] and self.board["a3"] != '   ':
            return self.verify_player(self.board["a3"])
        else:
            return [False]


check = {
    1: 2,
    2: 1
}
game = True
game_board = GameBoard()
position = 1
while game:
    player_turn = True
    game_board.print_board()
    while player_turn:
        player_turn = game_board.bet(position)
    game_board.print_board()
    verify_game = game_board.verify_game()
    if verify_game[0]:
        print(verify_game[1])
        game = False

    position = check[position]
