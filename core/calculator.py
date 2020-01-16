from core.decorators import cache_decorator

operations = ['+', '-', '/', '*', '**']


@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        try:
            return a/b
        except ZeroDivisionError:
            print('Делишь на ноль?! Только не здесь!')
            exit(0)
    elif operation == '*':
        return a*b
    else:
        return a**b


if __name__ == '__main__':
    try:
        a = int(input('Введите число: '))
        b = int(input('Введите число: '))
    except ValueError:
        print('Упс, ошибочка:( Калькулятор работает только с целыми числами от 0 до 9')
        exit(0)

    operation = input('Введите операцию: ')
    assert operation in operations, \
        print('Калькулятор поодерживает следующие операции: +, -, /, *, **. Вводить без кавычек!')

    print('Результат:', calculator(a, b, operation))
