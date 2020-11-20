import random

names = ['John', 'Ivan', 'Maksim', 'Olga', 'Irina', 'Anna', 'Alexander', 'Ingvar', 'Lars']


class Greeter:

    def __init__(self):
        self.name = random.choice(names)

    def greet(self):
        print(f"Greeting! I am robo-{self.name} at {hash(self)}")
