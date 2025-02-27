if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Sortujemy listę po ocenach
    students.sort(key=lambda x: x[1])

    # Tworzymy zbiór unikalnych ocen i wybieramy drugą najmniejszą
    unique_scores = sorted(set(s[1] for s in students))
    second_lowest_score = unique_scores[1]  # Druga najmniejsza ocena

    # Pobieramy studentów z tą oceną i sortujemy ich alfabetycznie
    second_score_students = sorted([s[0] for s in students if s[1] == second_lowest_score])

    for student in second_score_students:
        print(student)
