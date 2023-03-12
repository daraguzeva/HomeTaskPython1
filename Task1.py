# Найдите сумму цифр трехзначного числа.

num = int(input('Введите трехзначное число: '))
if num//1000 != 0:
    print('Число не трехзначное. Введите корректное число.')
else:
    unt = num % 10
    deff = num//10
    des = deff%10
    hund = deff//10
    summ = unt + des + hund

print(summ)
