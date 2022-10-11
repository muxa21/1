# import math
#
# figures = ["круг", "квадрат", "прямоугольник","треугольник" ]#"ромб"]
#
# def square():
#     a = float(input("введите сторону квадрата:"))
#     p = a * 4
#     s = a * a
#     b = a * 2 ** 0.5
#     print(f"Периметр = {round(p,2)}")
#     print(f"Площадь = {round(s,2)}")
#     print(f"Диагональ = {round(b, 2)}")
# #square(float(input()))
#
# def circle():
#     r = float(input("Введите радиус круга:"))
#     p = r * 2 * math.pi
#     d = 2 * r
#     s = r * r * math.pi
#     print(f"Длина окружности = {round(p, 2)}")
#     print(f"Диаметр = {round(d, 2)}")
#     print(f"Площадь круга = {round(s, 2)}")
# #circle(float(input()))
#
# def rectangle():
#     a = float(input("введите 1-ю сторону прямоугольника:"))
#     #while True:
#     #a =input().strip()
#     #if a.isdigit() and b.isdigit() and c.isdigit():
#      #   break
#     #else:
#         #print
#     b = float(input("введите 2-ю сторону прямоугольника:"))
#     p = (a + b) * 2
#     s = a * b
#     c = (a * a + b * b) ** 0.5
#     print(f"Периметр = {round(p,2)}")
#     print(f"Площадь = {round(s,2)}")
#     print(f"Диагональ = {round(c, 2)}")
# #rectangle(float(input("Введите 1-ую сторону прямоугольника \n")),float(input("Введите 2-ую сторону прямоугольника \n")))
#
# def triangle():
#     a = float(input("введите 1-ю сторону треугольника:"))
#     b = float(input("введите 2-ю сторону треугольника:"))
#     c = float(input("введите 3-ю сторону треугольника:"))
#     if a + b > c and b + c > a and a + c > b:
#         p = a + b + c
#         p2 = p / 2
#         s = (p2 * (p2 - a) * (p2 - b) * (p2 - c)) ** 0.5
#         print(f"Периметр = {round(p, 2)}")
#         print(f"Площадь = {round(s, 2)}")
#     else:
#         print("Такого треугольника не существует")
# #triangle(float(input("Введите 1-ую сторону треугольника \n")),
#          #float(input("Введите 2-ую сторону треугольника \n")),
#          #float(input("Введите 3-ую сторону треугольника \n")))
#
# #def rhombus_p():
#     #p = a * 4
#     #print(f"Периметр = {round(p, 2)}")
# #rhombus_p(float(input()))
#
# #def rhombus_s():
#     #s = a * b / 2
#     #print(f"Площадь = {round(s, 2)}")
# #rhombus_s(float(input("Введите 1-ую диагональ ромба \n")),float(input("Введите 2-ую диагональ ромба \n")))
#
# func_figures = [circle, square, rectangle, triangle]
# while True:
#     print("Выберите номер фигуры из предложенных:")
#     for i,figure in enumerate(figures,1):
#         print(f"{i}. {figure}")
#     a = input().strip()
#     if a.isdigit():
#         a = int(a) - 1
#         if  a < len(figures):
#             func_figures[a]()
#         else:
#             print("Вы ввели слишком большое число")
#     else:
#          print("Вы ввели не числo")



# def func():
#     '''
#     doing nothing
#     :return:
#     '''
#     pass
#
# func()

#a = []

# for i in range(100):
#     if i % 3 != 0:
#         a.append(i)
# print(a)


# a = (i ** 3 for i in range(100) if i % 3 != 0)
# print(next(a))
#
# for i in a:
#     print(i)

# def isMagicDate(day, month, year):
#     return str( day * month) == str(year)[2:4]
#
# print(isMagicDate(20, 12, 1960))

# isMagicDate = lambda day, month, year: str(day * month) == str(year)[-2:]
#
# print(isMagicDate(10, 6, 1960))
# get_cube = lambda  x : x **3
#
# print(get_cube(4))

# welcome = lambda user: print("Welcome " + user + "!")
#
# welcome("anon")


# get_prod = lambda a,b,c, : a * b * c
# print(get_prod(3,5,7))

# welcome = lambda : print("Welcome")
# welcome()


# def run_task(task):
#     print("Before running the task")
#     task()
#     print("After running the task")
#
# run_task(lambda : print("Task is compleate!"))
# important_task = lambda : print("Important task is compleate!")
# run_task(important_task)

# old_list = list(range(10000000))
#Rimport time, random

#start = time.time()
#
# new_list = []
# for item in old_list:
#     new_list.append(str(item))
# print(time.time() - start)
#
# # print(new_list)

# start = time.time()
#new_list = list(map(str, old_list))

# print(new_list)

# print(time.time() - start)
#
# old_list = [random.randint(0,1) for i in range(100)]
# new_list = list(filter(lambda x: x % 5 == 0, old_list))

# n = int(input('Enter a number : '))
# reversed = int(str(n)[::-1])
#print(int(str(6667)[::-1]))


















