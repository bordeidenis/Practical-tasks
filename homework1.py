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


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

except ValueError:
    print("Вы ввели не число")

else:
    print(get_color_name([a, b, c]))
