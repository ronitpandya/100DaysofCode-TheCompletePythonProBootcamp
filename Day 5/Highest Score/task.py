student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
maximum = 0
for scores in student_scores:
    if scores > maximum :
        maximum = scores
    elif scores < maximum :
        maximum = maximum
    else:
        maximum = maximum
print(maximum)

