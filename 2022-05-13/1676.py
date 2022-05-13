a = int(input())


def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


result = factorial(a)

count = 0
for i in range(2, a + 1):
    if i % 5 == 0:
        count += 1
    if i % 25 == 0:
        count += 1
    if i % 125 == 0:
        count += 1
print(count)
