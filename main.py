mesto = int(input('Введите номер места'))
if mesto % 2 == 0 and mesto <= 36:
    print('Верхнее место в купе')
elif mesto % 2 != 0 and mesto <= 35:
    print('Нижнее место в купе')
elif mesto % 2 == 0 and mesto > 36:
    print('Верхнее боковое место')
else:
    print('Нижнее боковое место')