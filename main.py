from greeter import Greeter

if __name__ == '__main__':
    try:
        i = int(input("Сколько раз Вас нужно приветствовать?: "))
        for _ in range(i):
            Greeter().greet()
    except ValueError:
        print("Введённые символы не являются целым числом!")
