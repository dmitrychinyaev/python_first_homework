number = int(input("Введите число:"))
result = 0
while(number > 0):
    ostatok = number % 10
    result = result + ostatok
    number = number//10
print("Сумма цифр равна: ", result)