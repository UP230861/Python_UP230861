# 1. Age input and driving feedback
age = int(input("1. Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# 2. Compare my_age and your_age
my_age = 25
your_age = int(input("\n2. Enter your age: "))
if your_age > my_age:
    diff = your_age - my_age
    print(f"You are {diff} year{'s' if diff > 1 else ''} older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    print(f"I am {diff} year{'s' if diff > 1 else ''} older than you.")
else:
    print("We are the same age.")

# 3. Compare two numbers
a = int(input("\n3. Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


#NIVEL 2
# 4. Grade based on score
score = int(input("\n4. Enter your score: "))
if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 79:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
elif 0 <= score <= 49:
    print("Grade: F")
else:
    print("Invalid score")

# 5. Check season by month
month = input("\n5. Enter month: ").capitalize()
if month in ['September', 'October', 'November']:
    print("Season: Autumn")
elif month in ['December', 'January', 'February']:
    print("Season: Winter")
elif month in ['March', 'April', 'May']:
    print("Season: Spring")
elif month in ['June', 'July', 'August']:
    print("Season: Summer")
else:
    print("Unknown month")

# 6. Fruit checker
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("\n6. Enter a fruit: ").lower()
if new_fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(new_fruit)
    print("Updated fruit list:", fruits)


#NIVEL 3
# 7. Person dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# a) Check if skills key exists, print middle skill
if 'skills' in person:
    skills = person['skills']
    mid_index = len(skills) // 2
    if len(skills) % 2 == 0:
        middle = skills[mid_index - 1:mid_index + 1]
    else:
        middle = [skills[mid_index]]
    print("\n7.a Middle skill(s):", middle)

# b) Check if 'Python' in skills
has_python = 'Python' in person['skills']
print("7.b Has Python skill:", has_python)

# c) Developer type
s = set(person['skills'])
if {'JavaScript', 'React'} == s:
    print("7.c He is a front end developer")
elif {'Node', 'Python', 'MongoDB'}.issubset(s):
    print("7.c He is a backend developer")
elif {'React', 'Node', 'MongoDB'}.issubset(s):
    print("7.c He is a fullstack developer")
else:
    print("7.c Unknown title")

# d) Check marital status and country
if person['is_marred'] and person['country'] == 'Finland':
    full_name = person['first_name'] + ' ' + person['last_name']
    print(f"7.d {full_name} lives in Finland. He is married.")
