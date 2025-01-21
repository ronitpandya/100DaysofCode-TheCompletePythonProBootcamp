programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


student_grades = {}
#logic for scores to grades

for name, value in student_scores.items():
    if value < 70 :
        student_grades[name] = "Fail"
    elif value < 81:
        student_grades[name] = "Acceptable"
    elif value < 91:
        student_grades[name] = "Exceeds Expectations"
    else:
        student_grades[name] = "Outstanding"

print(student_grades)