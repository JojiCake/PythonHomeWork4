from collections import Counter

nums = input("Введите числа через пробе: ").split()
counts = Counter(nums)
print([i for i in counts if counts [i] == 1])

res = []
for key in counts:
    if counts[key] == 1:
        res.append(key)
print(res)