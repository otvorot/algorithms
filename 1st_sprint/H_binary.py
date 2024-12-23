# Тимофей записал два числа в двоичной системе счисления и попросил Гошу
# вывести их сумму, также в двоичной системе. Встроенную в язык программирования
# возможность сложения двоичных чисел применять нельзя. Помогите Гоше решить задачу.

# Решение должно работать за O(N), где N –— количество разрядов максимального 
# числа на входе.

# Формат ввода
# Два числа в двоичной системе счисления, каждое на отдельной строке. Длина каждого
# числа не превосходит 10 000 символов.

# Формат вывода
# Одно число в двоичной системе счисления.


import sys
sys.set_int_max_str_digits(0)

def main():
    num1 = [int(i) for i in input()]
    num2 = [int(i) for i in input()]
    len1 = len(num1)
    len2 = len(num2)
    result = []
    add = 0
    
    if len1-len2 < 0: num1 = [0]*abs(len1-len2) + num1
    elif len1-len2 > 0: num2 = [0]*(len1-len2) + num2
    else: pass
    
    for i in range(1, len(num1)+1):
        if num1[-i] + num2[-i] + add == 2:
            add = 1
            result.append(0)
        elif num1[-i] + num2[-i] + add == 3:
            add = 1
            result.append(1)
        else:
            result.append(num1[-i] + num2[-i] + add)
            add = 0
    if add == 1: result.append(1)
    print(int(''.join(map(str, result[::-1]))))

if __name__ == '__main__':
    main()