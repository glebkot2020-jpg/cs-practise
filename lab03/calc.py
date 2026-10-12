a = float(input("Первое число: "))
b = float(input("Второе число: "))
op = input("Операция (+ - * /): ")

if op == "+":
    print("Результат:", a + b)
elif op == "-":
    print("Результат:", a - b)
elif op == "*":
    print("Результат:", a * b)
elif op == "/":
    if b == 0:
        print("Ошибка: деление на ноль")
    else:
        print("Результат:", a / b)
else:
    print("Неизвестная операция")
