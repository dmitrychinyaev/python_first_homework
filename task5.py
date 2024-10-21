number = int(input("Введите число (от 1 до 100000): "))

if number <= 1 or number > 100000:
    print("Некорректное число")
    exit()

for i in range(2, int(number**0.5)):
    if number % i == 0:
        print("Число составное")
        break
else:
    print("Число простое")
