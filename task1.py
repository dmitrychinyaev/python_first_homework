ask = int(input("Введите номер четверти: "))

if ask == 1:
    print("x>0, y>0")
elif ask == 2:
    print("x<0, y>0")
elif ask == 3:
    print("x<0, y<0")
elif ask == 4:
    print("x>0, y<0")
else:
    print("Неправильное число")