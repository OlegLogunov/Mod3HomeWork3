# Печать произвольных параметров
def test(*params):
    print('Печать произвольных параметров: ',*params)

test("Urban", 2024, True)
test(15, " апреля " , 2024, False)

# Расчет факториала
def factor_recurs(n):
    if n == 1:
        return n
    else:
        return n * factor_recurs(n - 1)

print("Введите целое положительное число для расчета факториала:")
val = int(input())
print(f'{val}! = {factor_recurs(val)}')
