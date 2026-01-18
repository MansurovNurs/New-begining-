#
#
# students = ['nursultan', 'nika', 'nurlis', 'saikal', 'elmira']
# map_students = list(map(lambda slow: slow.title(), students))
# print(map_students)
#
# filter_students = list(filter(lambda word: 'a' in word, students))
# print(filter_students)
#
# sorted_students = sorted(students, key=lambda word: word[0])
# print(sorted_students)
numbers = [34, 23, 32, 13, 36, 46]
target = 39
sort_by_closely = sorted(numbers, key=lambda x: abs(x - target))

print((target, sort_by_closely))

