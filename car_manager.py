from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        self.all_cars=[]
        self.initial_distance=STARTING_MOVE_DISTANCE
    def create_cars(self):
        new_car=Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2,stretch_wid=1)
        new_car.penup()
        new_car.goto(280,random.randint(-250,250))
        new_car.setheading(180)
        self.all_cars.append(new_car)
        
    def move_forward(self):
        for i in self.all_cars:
            i.forward(self.initial_distance)
        
    def increment(self):
        self.initial_distance+= MOVE_INCREMENT