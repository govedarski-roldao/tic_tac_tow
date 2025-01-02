from enum import verify


class GameBoard:
    def __init__(self):
        self.p_one = " X "
        self.p_two = " O "
        self.board = {
            'a1': '   ', 'a2': '   ', 'a3': '   ',
            'b1': '   ', 'b2': '   ', 'b3': '   ',
            'c1': '   ', 'c2': '   ', 'c3': '   ',
        }

    def print_board(self):
        print(f"{self.board['a1']}|{self.board['a2']}|{self.board['a3']}")
        print("------------")
        print(f"{self.board['b1']}|{self.board['b2']}|{self.board['b3']}")
        print("------------")
        print(f"{self.board['c1']}|{self.board['c2']}|{self.board['c3']}")

    def place_play(self, player, column, line):
        if player == "p_one":
            self.board[f"{column}{line}"] = self.p_one
        else:
            self.board[f"{column}{line}"] = self.p_two

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


game = True
game_board = GameBoard()
while game:
    game_board.print_board()
    player_one_column = input("Player One, which is the column? A, B, C?")
    player_one_line = input("And what is the line?1, 2 or 3?")
    game_board.place_play("p_one", player_one_column, player_one_line)
    game_board.print_board()
    player_two_column = input("Player Two, which is the column? A, B, C?")
    player_two_line = input("And what is the line?1, 2 or 3?")
    game_board.place_play("p_two", player_two_column, player_two_line)
    verify_game = game_board.verify_game()
    if verify_game[0]:
        print(verify_game[2])
        game = False
