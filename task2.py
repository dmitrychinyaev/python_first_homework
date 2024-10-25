first_point_x= int(input("Введите координату Х первой точки: "))
first_point_y = int(input("Введите координату Y первой точки: "))

second_point_x = int(input("Введите координату Х второй точки: "))
second_point_y = int(input("Введите координату Y второй точки: "))

result = ((first_point_x - first_point_y)**2 + (second_point_x - second_point_y)**2)**0.5

print(result)