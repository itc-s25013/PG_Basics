list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
answers = []

for a in list1:
    for b in list2:
        answers.append(a * b)

print(answers)
