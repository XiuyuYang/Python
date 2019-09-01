import random


class Game(object):
    def __init__(self, start_times, dice_per_person):
        self.start_times = start_times
        self.dice_per_person = dice_per_person
        self.player1 = Person(self.dice_per_person)
        self.player1.name = "Player01"
        self.player2 = Person(self.dice_per_person)
        self.player2.name = "Player02"

    def start(self):
        for per_game in range(self.start_times):
            self.game_play(per_game)
            self.win()
            self.player1.score = []
            self.player2.score = []

    def game_play(self, game_number):
        print("\nThis is the No.%s game:" % (game_number + 1))
        self.player1.roll_dices(self.dice_per_person)
        print("-" * 40)
        self.player2.roll_dices(self.dice_per_person)

    def win(self):
        def total(score):
            sum_num = 0
            for i in score:
                sum_num += i
            return sum_num

        if total(self.player1.score) > total(self.player2.score):
            print(self.player1.name, "WIN!")
        elif total(self.player1.score) < total(self.player2.score):
            print(self.player2.name, "WIN!")
        else:
            print("The score was tied.")


class Person(object):
    def __init__(self, dice_per_person):
        self.dice = Dice()
        self.dice_per_person = dice_per_person
        self.name = "Player"
        self.score = []
        self.dice_time = 1

    def roll_dices(self, dice_per_person):
        for roll in range(dice_per_person):
            count = self.roll_dice()
            print(self.name, "rolled <<", count, ">> at the", self.dice_time, "time.")
            self.dice_time += 1
            self.score.append(count)
        self.dice_time = 1

    def roll_dice(self):
        return self.dice.roll()


class Dice:
    def __init__(self):
        pass

    def roll(self):
        count = random.randint(1, 6)
        # print(count)
        return count


if __name__ == '__main__':
    g = Game(3, 5)
    g.start()
