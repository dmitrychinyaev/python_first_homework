num = int(input("Введите число: "))

if (num % 5 == 0 and (num % 10 == 0 or num % 15 != 0)) and num % 30 != 0:
    print("Число подходит")
else:
    print("Число не подходит") 