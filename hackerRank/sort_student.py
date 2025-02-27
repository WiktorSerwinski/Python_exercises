if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    students.sort(key= lambda x: x[1])
    # print(students)
    second_score_student_score=students[0][1]
    second_score_student_name=students[0][0]
    second_score_students=[]
    # print(second_score_student_score)
    for s in students:
        if(s[1]> second_score_student_score):
            second_score_student_score = s[1]
            second_score_student_name = s[0]
            second_score_students.append(s)
            break
    for s in students:
        if(s[1]==second_score_student_score and s[0]!=second_score_student_name):
            second_score_students.append(s)

    second_score_students.sort(key= lambda x: x[0])
    for s in second_score_students:
        print(s[0])

    