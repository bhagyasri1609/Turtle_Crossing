import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
scoreboard=Scoreboard()
car_manager=CarManager()
screen.listen()
screen.onkey(player.go_up,"Up")
count=0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    count+=1
    if count==6:
        car_manager.create_cars() 
        count=0
    car_manager.move_forward()
    for cars in car_manager.all_cars:
        if player.distance(cars)<=20:
            scoreboard.game_over()
            game_is_on=False
    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.level_increment()
        car_manager.increment()
    screen.update()
    
screen.exitonclick()
