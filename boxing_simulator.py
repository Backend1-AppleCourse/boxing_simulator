import random

class DamageJudge:
    def __init__(self):
        self.rules = [{'move': 1, 'wins_against': [2,4], 'loses_against': [3]},
                      {'move': 2, 'wins_against': [3], 'loses_against': [4,1]},
                      {'move': 3, 'wins_against': [4], 'loses_against': [1]},
                      {'move': 4, 'wins_against': [1], 'loses_against': [2]}]
    def compare(self, move1, move2):
        for rule in self.rules:
            if rule['move'] == move1:
                if move2 in rule['wins_against']:
                    return 1
                elif move2 in rule['loses_against']:
                    return -1
                else:
                    return 0

class Fighter:
    def __init__(self, name):
        self.name = name
    def attack(self):
        move = input(f"{self.name}, enter your move (1, 2, 3, 4): ")
        while move not in ['1', '2', '3', '4']:
            print("Invalid move. Enter 1, 2, 3, or 4.")
            move = input(f"{self.name}, enter your move (1, 2, 3, 4): ")
        move = int(move)
        return move

class Enemy(Fighter):
    def attack(self):
        return random.randint(1, 4)

class Game:
    def __init__(self):
        self.player = Fighter("Player")
        self.enemy = Enemy("Enemy")
        self.judge = DamageJudge()
    def play(self):
        result = self.judge.compare(self.player.attack(), self.enemy.attack())
        if(result == 0):
            print("It's a draw!")
        elif(result == 1):
            print(f"{self.player.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")

game = Game()
game.play()