numbers = list(map(lambda x: int(x), input().split(', ')))
result = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        result.append(i)

print(result)
