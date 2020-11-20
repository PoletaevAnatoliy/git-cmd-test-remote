from greeter import Greeter

if __name__ == '__main__':
    try:
        i = input("Сколько раз Вас нужно приветствовать (введите целое число, например, 2)?: ")
        for _ in range(int(i)):
            Greeter().greet()
    except ValueError:
        print(f"Введённые Вами символы (\"{i}\") не являются целым числом!")
