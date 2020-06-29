import random

x = input("Введите первое число")
y = input("Введите второе число")
i = random.randint(int(x), int(y))
def func():
    answer = input("Ваш ответ")
    if int(answer) == int(i):
        print("Ура!")
    elif int(answer) > int(i):
        print("Загаданное число меньше")
        func()
    elif int(answer) < int(i):
        print("Заданное число больше")
        func()
func()



