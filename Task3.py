# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр
# равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

num = int(input('Введите номер билета: '))
no_1 = num % 10
deff = num//10
no_2 = deff % 10
deff = deff//10
no_3 = deff % 10
summ_1 = no_1 + no_2 + no_3
deff = deff//10
no_4 = deff % 10
deff = deff//10
no_5 = deff % 10
no_6 = deff//10
summ_2 = no_4 + no_5 + no_6
if summ_1 == summ_2:
    print('Счастливый билетик :)')
else:
    print('Билетик не счастливый :(')
