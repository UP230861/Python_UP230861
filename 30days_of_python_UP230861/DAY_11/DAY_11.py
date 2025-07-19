import math
from collections import Counter
import keyword

print("\n--- LEVEL 1 ---")

# 1. Add two numbers
def add_two_numbers(a, b):
    return a + b
print("Add:", add_two_numbers(5, 7))

# 2. Area of a circle
def area_of_circle(r):
    return math.pi * r * r
print("Area of circle:", area_of_circle(3))

# 3. Add all numbers (check types)
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "All inputs must be numbers"
print("Sum of all nums:", add_all_nums(1, 2, 3.5))

# 4. Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
print("25C to F:", convert_celsius_to_fahrenheit(25))

# 5. Check season
def check_season(month):
    month = month.capitalize()
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    return 'Invalid month'
print("Season in April:", check_season("April"))

# 6. Calculate slope
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
print("Slope:", calculate_slope(1, 2, 3, 6))

# 7. Solve quadratic equation
def solve_quadratic_eqn(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return "No real solution"
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    return (x1, x2)
print("Quadratic roots:", solve_quadratic_eqn(1, -3, 2))

# 8. Print list
def print_list(lst):
    for item in lst:
        print(item)
print("Print list:")
print_list(['apple', 'banana', 'cherry'])

# 9. Reverse list
def reverse_list(lst):
    result = []
    for i in range(len(lst)-1, -1, -1):
        result.append(lst[i])
    return result
print("Reverse list (nums):", reverse_list([1, 2, 3, 4, 5]))
print("Reverse list (letters):", reverse_list(["A", "B", "C"]))

# 10. Capitalize list
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]
print("Capitalize:", capitalize_list_items(['apple', 'banana']))

# 11. Add item
def add_item(lst, item):
    lst.append(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
print("Add Meat:", add_item(food_staff, 'Meat'))
print("Add 5:", add_item(numbers, 5))

# 12. Remove item
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
print("Remove Mango:", remove_item(food_staff, 'Mango'))
print("Remove 3:", remove_item(numbers, 3))

# 13. Sum of numbers
def sum_of_numbers(n):
    return sum(range(n + 1))
print("Sum to 5:", sum_of_numbers(5))
print("Sum to 10:", sum_of_numbers(10))
print("Sum to 100:", sum_of_numbers(100))

# 14. Sum of odds
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)
print("Sum of odds to 10:", sum_of_odds(10))

# 15. Sum of evens
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)
print("Sum of evens to 10:", sum_of_even(10))

#NIVEL 2
print("\n--- LEVEL 2 ---")

# 1. Count evens and odds
def evens_and_odds(n):
    evens = len([i for i in range(n + 1) if i % 2 == 0])
    odds = len([i for i in range(n + 1) if i % 2 != 0])
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."
print(evens_and_odds(100))

# 2. Factorial
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print("Factorial of 5:", factorial(5))

# 3. Check if empty
def is_empty(param):
    return not bool(param)
print("Is empty:", is_empty(""))

# 4. Stats functions
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    return lst[mid] if n % 2 != 0 else (lst[mid - 1] + lst[mid]) / 2

def calculate_mode(lst):
    freq = Counter(lst)
    max_count = max(freq.values())
    return [k for k, v in freq.items() if v == max_count]

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))

sample = [4, 2, 5, 8, 6, 2]
print("Mean:", calculate_mean(sample))
print("Median:", calculate_median(sample))
print("Mode:", calculate_mode(sample))
print("Range:", calculate_range(sample))
print("Variance:", calculate_variance(sample))
print("Std Dev:", calculate_std(sample))

#NIVEL 3
print("\n--- LEVEL 3 ---")

# 1. Is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
print("Is 7 prime?", is_prime(7))

# 2. All items unique
def all_unique(lst):
    return len(lst) == len(set(lst))
print("All unique:", all_unique([1, 2, 3, 4]))

# 3. All same type
def same_type(lst):
    return all(type(item) == type(lst[0]) for item in lst)
print("Same type:", same_type([1, 2, 3]))

# 4. Valid Python variable
def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)
print("Is 'my_var' valid?", is_valid_variable("my_var"))
print("Is 'for' valid?", is_valid_variable("for"))

# 5. Most spoken languages
countries_data = [
    {'name': 'India', 'languages': ['Hindi', 'English'], 'population': 1380004385},
    {'name': 'USA', 'languages': ['English'], 'population': 331002651},
    {'name': 'Brazil', 'languages': ['Portuguese'], 'population': 212559417},
    {'name': 'Nigeria', 'languages': ['English'], 'population': 206139589},
    {'name': 'Mexico', 'languages': ['Spanish'], 'population': 128932753},
]
def most_spoken_languages(n=10):
    langs = []
    for country in countries_data:
        langs.extend(country['languages'])
    freq = Counter(langs)
    return freq.most_common(n)
print("Most spoken languages:", most_spoken_languages())

# 6. Most populated countries
def most_populated_countries(n=10):
    sorted_pop = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_pop[:n]
print("Most populated countries:", most_populated_countries())
