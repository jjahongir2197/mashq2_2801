class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lives = 3

    def play(self, points):
        self.score += points
        self.lives -= 1

    def info(self):
        return f"{self.name} | Ball: {self.score} | Jon: {self.lives}"


class Arcade:
    def __init__(self):
        self.players = []

    def add_player(self, p):
        self.players.append(p)

    def show(self):
        for p in self.players:
            print(p.info())


arc = Arcade()

while True:
    print("\n1.O‘yinchi 2.O‘ynash 3.Hisobot 0.Exit")
    c = input(">>> ")

    if c == "1":
        arc.add_player(Player(input("Ism: ")))
    elif c == "2":
        i = int(input("Index: "))
        arc.players[i].play(int(input("Ball: ")))
    elif c == "3":
        arc.show()
    elif c == "0":
        break
