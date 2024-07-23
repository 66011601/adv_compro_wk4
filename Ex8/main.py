#Assignment 8: Filtering and Modifying a List of Student Grades
#1. Define a list of integers named `grades` containing student grades.
grades = [55, 70, 65, 40, 90, 85, 50, 77]
#2. Use a list comprehension to create a new list named `passed_with_bonus` that:
#    - Filters the grades to include only those that are 60 and above.
#    - Applies a 5% bonus to each of the filtered grades.
passed_with_bonus = list(map(lambda y: (0.05*y)+y, filter(lambda x: x>=60, grades)))
#3. Print the `passed_with_bonus` list to display the modified grades.
print(f"Grades after filtering and applying bonus: {passed_with_bonus}")
#Expected Output:
#Grades after filtering and applying bonus: [73.5, 68.25, 94.5, 89.25, 80.85]