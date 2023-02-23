file_path = "./colors.txt"
with open(file_path, "r") as file:
    colors = eval(file.read())


def get_color_name(color_code):
    for key, value in colors.items():
        if value == color_code:
            return key
    return ("Такого цвета не существует")

a = int(input("Введите первое число: "))
b= int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
print(get_color_name([a, b, c]))
