def gradingStudents(grades):
    for i, grade in enumerate(grades):
        modulus = grade % 5
        if grade < 38:
            grade = grade
        elif modulus == 4:
            grade = grade + 1
        elif modulus == 3:
            grade = grade + 2
        grades[i] = grade

    return grades


if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))

    print(gradingStudents(arr))
