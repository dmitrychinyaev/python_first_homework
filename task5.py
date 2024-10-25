BORDER_FROM = 1
BORDER_TO = 100000

number = int(input("Введите число (от 1 до 100000): "))

if number <= BORDER_FROM or number > BORDER_TO:
    print("Некорректное число")
    exit()

for i in range(2, int(number**0.5)):
    if number % i == 0:
        print("Число составное")
        break
else:
    print("Число простое")
