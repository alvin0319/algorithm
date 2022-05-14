def calculate_grade(grade: int) -> str:
    if grade >= 90:
        return "A"
    elif 90 > grade >= 80:
        return "B"
    elif 80 > grade >= 70:
        return "C"
    elif 70 > grade >= 60:
        return "D"
    else:
        return "F"


print(calculate_grade(int(input())))
