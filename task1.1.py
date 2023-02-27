# я пробовал перевести файл colors.txt в формат JSON, однако получал исключение при работе с ним
# JSONDecodeError: Expecting property name enclosed in double quotes:
# искал решение здесь https://bobbyhadz.com/blog/python-jsondecodeerror-expecting-property-name-enclosed-in-double-quotes
# import json
file_path = "./colors.txt"
with open(file_path, "r") as file:
    colors = eval(file.read())


#    valid_colors = file.read()
#    colors = json.loads(valid_colors)


def get_color_name(color_code):
    for key, value in colors.items():
        if value == color_code:
            return key
    return ("Такого цвета не существует")


def get_color_code(color_name):
    if color_name in colors:
        return colors[color_name]
    return ("Такого цвета не существует")


def count_color_greater_than_0():
    counter = 0
    for num in colors.values():
        if sum([1 for i in num if i > 0]) == 1:
            counter += 1
    return counter

try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

except ValueError:
    print("Вы ввели не число")

else:
    print(get_color_name([a, b, c]))

name = input("Введите название цвета: ")
print(get_color_code(name))

print("Цветов, где только одно число больше 1: ", count_color_greater_than_0())
