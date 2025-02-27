from functools import reduce


n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = [float(x) for x in line]
    student_marks[name] = scores
query_name = input()
mark_mean =  sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{mark_mean:.2f}")

# average = reduce(lambda acc, n: acc*n,marks_list)