python
import math

def calculator():
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")

    choice = input("Выберите операцию (1-10): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            result = num1 + num2
            print("Результат: ", result)
        elif choice == '2':
            result = num1 - num2
            print("Результат: ", result)
        elif choice == '3':
            result = num1 * num2
            print("Результат: ", result)
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print("Результат: ", result)
            else:
                print("Ошибка: Деление на ноль!")

    elif choice == '5':
        num1 = float(input("Введите число: "))
        power = float(input("Введите степень: "))
        result = math.pow(num1, power)
        print("Результат: ", result)

    elif choice == '6':
        num = float(input("Введите число: "))
        if num >= 0:
            result = math.sqrt(num)
            print("Результат: ", result)
        else:
            print("Ошибка: Корень из отрицательного числа!")

    elif choice == '7':
        num = int(input("Введите число: "))
        result = math.factorial(num)
        print("Результат: ", result)

    elif choice in ['8', '9', '10']:
        angle = float(input("Введите угол в градусах: "))
        radians = math.radians(angle)

        if choice == '8':
            result = math.sin(radians)
            print("Результат: ", result)
        elif choice == '9':
            result = math.cos(radians)
            print("Результат: ", result)
        elif choice == '10':
            result = math.tan(radians)
            print("Результат: ", result)

    else:
        print("Ошибка: Некорректный выбор операции!")

calculator()

