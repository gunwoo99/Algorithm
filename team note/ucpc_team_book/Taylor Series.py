from decimal import Decimal
fact = [Decimal('0') for _ in range(40)]
fact[1] = Decimal('1')
for i in range(2, 40):
    fact[i] = Decimal(str(i)) * fact[i - 1]

def sin(x: Decimal):
    x %= 2 * Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421179821')
    res = Decimal('0')
    value = x
    for k in range(19):
        addition = (-1 if k % 2 == 1 else 1) * (value / fact[2 * k + 1])
        res += addition
        value *= x * x
    return res