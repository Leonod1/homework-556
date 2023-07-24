check = int(input('Сколько стоит товар: '))
summ = 0

for sym in(1, check):
    check /= 4
    summ += check
    print('Hello', summ)

print()
print('Этот товар', check)

