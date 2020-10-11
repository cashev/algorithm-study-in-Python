data = [9, 4, 5, 2, 8, 3, 7, 8, 3, 2, 6, 5, 7, 9, 2, 9]

array = [0 for _ in range(10)]

for i in data:
  array[i] += 1

result = []
for i in range(10):
  if array[i] > 0:
    result += [i] * array[i]

print(result)
