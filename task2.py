FIRST_POINT_X = int(input("Введите координату Х первой точки: "))
FIRST_POINT_Y = int(input("Введите координату Y первой точки: "))

SECOND_POINT_X = int(input("Введите координату Х второй точки: "))
SECOND_POINT_Y = int(input("Введите координату Y второй точки: "))

result = ((FIRST_POINT_X - SECOND_POINT_X)**2 + (SECOND_POINT_X - SECOND_POINT_Y)**2)**0.5

print(result)