# 1. Create an empty dictionary called dog
dog = {}
print("1. Empty dog dictionary:", dog)

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Max'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
print("2. Dog dictionary:", dog)

# 3. Create a student dictionary and add required keys
student = {
    'first_name': 'Juan',
    'last_name': 'Pérez',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'Git'],
    'country': 'Mexico',
    'city': 'CDMX',
    'address': '123 Calle Falsa'
}
print("3. Student dictionary:", student)

# 4. Get the length of the student dictionary
print("4. Length of student dictionary:", len(student))

# 5. Get the value of skills and check the data type, it should be a list
skills = student['skills']
print("5. Skills:", skills)
print("   Type of skills:", type(skills))

# 6. Modify the skills values by adding one or two skills
student['skills'].extend(['JavaScript', 'SQL'])
print("6. Updated skills:", student['skills'])

# 7. Get the dictionary keys as a list
keys_list = list(student.keys())
print("7. Keys of student dictionary:", keys_list)

# 8. Get the dictionary values as a list
values_list = list(student.values())
print("8. Values of student dictionary:", values_list)

# 9. Change the dictionary to a list of tuples using items() method
items_list = list(student.items())
print("9. Dictionary as list of tuples:", items_list)

# 10. Delete one of the items in the dictionary
del student['marital_status']
print("10. Deleted 'marital_status':", student)

# 11. Delete one of the dictionaries
del dog
print("11. 'dog' dictionary deleted.")
