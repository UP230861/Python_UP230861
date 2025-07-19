# 1. Add two numbers
def add_two_numbers(a, b):
    return a + b

# 2. Area of a circle
import math
def area_of_circle(r):
    return math.pi * r * r

# 3. Add all nums (arbitrary args, check types)
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "All inputs must be numbers"

# 4. Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

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

# 6. Calculate slope (y2 - y1)/(x2 - x1)
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# 7. Solve quadratic equation
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solution"
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return x1, x2

# 8. Print list
def print_list(lst):
    for item in lst:
        print(item)

# 9. Reverse list using loop
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# 10. Capitalize list items
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# 11. Add item to list
def add_item(lst, item):
    lst.append(item)
    return lst

# 12. Remove item from list
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# 13. Sum of numbers in range
def sum_of_numbers(n):
    return sum(range(n + 1))

# 14. Sum of odd numbers
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# 15. Sum of even numbers
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

#NIVEL 2
# 1. Count evens and odds
def evens_and_odds(n):
    evens = len([i for i in range(n + 1) if i % 2 == 0])
    odds = len([i for i in range(n + 1) if i % 2 != 0])
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

# 2. Factorial
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 3. Check if variable is empty
def is_empty(param):
    return not bool(param)

# 4. Statistical functions
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    return (sorted_lst[mid] if n % 2 != 0 
            else (sorted_lst[mid - 1] + sorted_lst[mid]) / 2)

from collections import Counter
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


#NIVEL 3
# 1. Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 2. Check all items unique in a list
def all_unique(lst):
    return len(lst) == len(set(lst))

# 3. Check if all items are of the same type
def same_type(lst):
    return all(type(item) == type(lst[0]) for item in lst)

# 4. Check valid Python variable
import keyword
def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)

# 5. Most spoken languages
from countries_data import countries_data
def most_spoken_languages(n=10):
    all_languages = []
    for country in countries_data:
        all_languages.extend(country['languages'])
    language_freq = Counter(all_languages)
    return language_freq.most_common(n)

# 6. Most populated countries
def most_populated_countries(n=10):
    sorted_pop = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_pop[:n]
