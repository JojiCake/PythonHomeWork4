import random

num_n = int(input("Введите число: "))
if num_n == 0:
    num = 1
str_line = ""
count = num_n

for i in range(num_n):
    new_n = random.randrange(0,101)
    while count > 1:
        new_n = random.randrange(0, 101)
        string = (f"{new_n}*x^{count} + ")
        str_line += string
        count -= 1
    if i == num_n - 1:
        string = (f"{new_n}*x ")
        str_line += string
    if i == num_n - 1 or i == num_n:
        string = (f"+ {new_n} = 0")
        str_line += string 
print(f"{str_line}")
with open("result.txt", "w") as data:
    data.write(str_line)
