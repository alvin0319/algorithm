numbers = []

n = int(input())

for i in range(0, n):
    numbers.append(input().split())


def split_char(words: str) -> list:
    return [word for word in words]


for i in range(len(numbers)):
    data = numbers[i]
    if len(data) >= 2:
        num, word = data
        words = split_char(word)

        newChar = ""
        for word in words:
            newChar = newChar + (int(num) * word)
        print(newChar)
