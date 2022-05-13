a = int(input())


def f(n: int) -> int:
    result = []
    for i in range(0, n + 1):
        if i == 0 or i == 1:
            result.append(i)
        else:
            first_previous = result[i - 1]
            second_previous = result[i - 2]
            result.append(first_previous + second_previous)
    return result[len(result) - 1]


print(f(a))
