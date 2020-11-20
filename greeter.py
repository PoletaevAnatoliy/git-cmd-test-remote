import random

names = ['John', 'Ivan', 'Maksim', 'Olga', 'Irina']


class Greeter:

    def __init__(self):
        self.name = random.choice(names)

    def __hash__(self):
        return hash(random.randint(1, 100))

    def greet(self):
        print(f"Greeting! I am robo-{self.name} at {hash(self)}")
