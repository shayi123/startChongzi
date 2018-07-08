from operator import itemgetter

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print('by_name_item: ', sorted(students, key=itemgetter(0)))
print('by_score_item: ', sorted(students, key=itemgetter(1)))
print('by_score_item: ', sorted(students, key=lambda t: t[1]))
print('by_score_item: ', sorted(students, key=itemgetter(1), reverse=True))


