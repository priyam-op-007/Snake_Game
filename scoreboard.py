from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score = {self.count}", False, "center", ('Courier', 15, 'bold'))

    def increase_score(self):
        self.clear()
        self.count += 1
        self.write(f"Score = {self.count}", False, "center", ('Ariel', 15, 'bold'))

    def final_score(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Your Final Score is {self.count}", False, "center", ('Ariel', 15, 'bold'))
