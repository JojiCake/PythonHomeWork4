import math

def calc_factor(num):
    result = 0
    while num % 1> 0:
        num *= 10
        result += 1
    return result

fract_accur = float (input("Введите необходимую точность: "))
rounded_pi = round(math.pi, calc_factor(fract_accur))
print(rounded_pi)