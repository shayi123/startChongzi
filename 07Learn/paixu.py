from _operator import itemgetter

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按名字正序
print(sorted(students, key=itemgetter(0)))
# 按成绩从低到高
print(sorted(students, key=lambda t: t[1]))
# 按成绩从高到低
print(sorted(students, key=itemgetter(1), reverse=True))
