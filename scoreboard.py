from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score=0
        self.update_level()
        
    def update_level(self):
        self.clear()
        self.goto(-280,250)
        self.write(arg=f"LEVEL: {self.score}",move=False,align="left",font=FONT)

    def level_increment(self):
        self.score+=1
        self.update_level()
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",move=False,align="center",font=FONT)
    