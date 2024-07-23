#Assignment 9: Filtering Eligible Children for a Fun Park
#1. Define a list of dictionaries named `children`, where each dictionary contains a `name`, `age`, and `height`.
children = [ 
    {"name": "Alice", "age": 2, "height": 95}, 
    {"name": "Bob", "age": 4, "height": 105}, 
    {"name": "Charlie", "age": 3, "height": 110}, 
    {"name": "David", "age": 5, "height": 102}, 
    {"name": "Eve", "age": 6, "height": 99} 
    ]
#2. Use a list comprehension to create a new list named `eligible_children` that:
#    - Filters the children to include only those with age greater than 3 and height greater than 100 cm.
eligible_children = list(filter(lambda x: True if x["age"] > 3 and x["height"] > 100 else False, children))
#3. Print the `eligible_children` list to display the names, ages, and heights of the eligible children.
print(f"Eligible children for the fun park: {eligible_children}")
#**Expected Output:**
#Eligible children for the fun park: [{'name': 'Bob', 'age': 4, 'height': 105}, {'name': 'David', 'age': 5, 'height': 102}]