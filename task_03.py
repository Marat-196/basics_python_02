# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и
# знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions
import fractions

a1 = list(map(int, input('Введите первое дробное число через символ "/": ').split('/')))
a2 = list(map(int, input('Введите второе дробное число через символ "/": ').split('/')))

s_frac_num = a1[0] * a2[1] + a2[0] * a1[1]
s_frac_denom = a1[1] * a2[1]
print('-' * 50)
print(f'Сумма дробей расчетная равна: {s_frac_num}/{s_frac_denom}')
print('Сумма дробей с использованием функции:', fractions.Fraction(a1[0], a1[1]) + fractions.Fraction(a2[0], a2[1]))
print('-' * 50)

p_frac_num = a1[0] * a2[0]
p_frac_denom = a1[1] * a2[1]

print(f'Произведение дробей расчетное равно: {p_frac_num}/{p_frac_denom}')
print('Произведение дробей с использованием функции:',
      fractions.Fraction(a1[0], a1[1]) * fractions.Fraction(a2[0], a2[1]))
