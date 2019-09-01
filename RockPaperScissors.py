import random


class RockPaperScissors(object):
    def __init__(self):
        self.player_1 = Player()
        self.player_1.name = "Player01"
        self.player_2 = Player()
        self.player_2.name = "Player02"
        self.round = 1
        pass

    def start(self):
        for i in range(1, self.round + 1):
            print("\nGame start, round", i)
            self.game()

    def game(self):
        result_player_01 = self.player_1.play()
        result_player_02 = self.player_2.play()
        print(self.player_1.name, result_player_01, "vs", self.player_2.name, result_player_02)
        self.win(result_player_01, result_player_02)
        pass

    def win(self, result_01, result_02):
        winner = self.player_1
        if result_01 == result_02:
            print("It was tied.")
            return
        elif result_01 == "rock":
            if result_02 == "paper":
                winner = self.player_2
        elif result_01 == "paper":
            if result_02 == "scissors":
                winner = self.player_2
        else:
            if result_02 == "scissors":
                winner = self.player_2
        print(winner.name, "WIN!")


class Player(object):
    def __init__(self):
        self.name = "Player's name"
        self.result_list = ["rock", "paper", "scissors"]
        pass

    def __str__(self):
        return self.name

    def play(self):
        result_index = random.randint(0, 2)
        return self.result_list[result_index]


if __name__ == '__main__':
    game = RockPaperScissors()
    game.player_1.name = "P1"
    game.player_2.name = "P2"
    game.round = 10
    game.start()
