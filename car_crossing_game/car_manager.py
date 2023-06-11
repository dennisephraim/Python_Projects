from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            rand_car = Turtle()
            rand_car.penup()
            rand_car.color(random.choice(COLORS))
            rand_car.shape("square")
            rand_car.setheading(180)
            rand_car.turtlesize(stretch_len=2)
            random_y = random.randint(-250, 250)
            rand_car.goto(300, random_y)
            self.all_cars.append(rand_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


