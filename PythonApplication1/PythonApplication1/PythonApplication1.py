python
import math

def calculator():
    print("��������� ��������:")
    print("1. ��������")
    print("2. ���������")
    print("3. ���������")
    print("4. �������")
    print("5. ���������� � �������")
    print("6. ���������� ������")
    print("7. ���������")
    print("8. �����")
    print("9. �������")
    print("10. �������")

    choice = input("�������� �������� (1-10): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("������� ������ �����: "))
        num2 = float(input("������� ������ �����: "))

        if choice == '1':
            result = num1 + num2
            print("���������: ", result)
        elif choice == '2':
            result = num1 - num2
            print("���������: ", result)
        elif choice == '3':
            result = num1 * num2
            print("���������: ", result)
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print("���������: ", result)
            else:
                print("������: ������� �� ����!")

    elif choice == '5':
        num1 = float(input("������� �����: "))
        power = float(input("������� �������: "))
        result = math.pow(num1, power)
        print("���������: ", result)

    elif choice == '6':
        num = float(input("������� �����: "))
        if num >= 0:
            result = math.sqrt(num)
            print("���������: ", result)
        else:
            print("������: ������ �� �������������� �����!")

    elif choice == '7':
        num = int(input("������� �����: "))
        result = math.factorial(num)
        print("���������: ", result)

    elif choice in ['8', '9', '10']:
        angle = float(input("������� ���� � ��������: "))
        radians = math.radians(angle)

        if choice == '8':
            result = math.sin(radians)
            print("���������: ", result)
        elif choice == '9':
            result = math.cos(radians)
            print("���������: ", result)
        elif choice == '10':
            result = math.tan(radians)
            print("���������: ", result)

    else:
        print("������: ������������ ����� ��������!")

calculator()

