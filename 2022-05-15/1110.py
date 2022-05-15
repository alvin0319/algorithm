n = input()


# 문자열을 한개씩 쪼개서 list로 반환
def split(word: str) -> list:
    return [char for char in word]


def new_char(current_char: str) -> str:
    # 문자열을 쪼갬, ex) 26 -> [2, 6]
    prev, next = map(int, split(current_char))
    # 쪼갠 문자열을 더한 후 str화
    result = str((prev + next))
    # str화한 문자열이 한 자리라면 앞에 0을 붙여줌
    if len(result) < 2:
        result = f"0{result}"
    # str화한 문자열을 다시 쪼갬
    new_prev, new_next = map(int, split(result))
    # 맨 처음 쪼갠 문자열의 마지막 값과 새로 쪼갠 문자열의 마지막 값을 더함
    new_char = str(f"{next}{new_next}")
    return new_char


if len(n) < 2:
    n = f"0{n}"

currentChar = new_char(n)

step = 1
while currentChar != n:
    currentChar = new_char(currentChar)
    step += 1

print(step)
