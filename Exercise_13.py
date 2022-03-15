

def operation(number1, number2, symbol):
    if symbol == '+':
        return number1 + number2
    elif symbol == '-':
        return number1 - number2
    elif symbol == '*':
        return number1 * number2
    elif symbol == '/':
        return number1 / number2


print(operation(5, 3, '*'))