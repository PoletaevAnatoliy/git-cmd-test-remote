from greeter import Greeter

if __name__ == '__main__':
    i = int(input("Сколько раз Вас нужно приветствовать?"))
    for _ in range(i):
        Greeter().greet()
