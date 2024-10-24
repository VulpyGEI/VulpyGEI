# Инициализация переменных
inputValue = ''
maxValue = 0
maxInputValue = ''

while inputValue != '0':
    inputValue = input('Введите число: ')

    if inputValue != '0':
        localValue = 0

        for item in inputValue:
            localValue += int(item)

        # Проверка, является ли текущая сумма цифр больше, чем максимальная
        if localValue > maxValue:
            maxValue = localValue
            maxInputValue = inputValue

print(f'Число с максимальной суммой цифр: {maxInputValue}')
input('Нажмите  Enter,  чтобы  закрыть  программу...')
