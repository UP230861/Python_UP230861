# 1. Iterate 0 to 10 using for loop and while loop
print("1. For loop from 0 to 10:")
for i in range(11):
    print(i, end=' ')
print("\n\nWhile loop from 0 to 10:")
i = 0
while i <= 10:
    print(i, end=' ')
    i += 1

# 2. Iterate 10 to 0 using for loop and while loop
print("\n\n2. For loop from 10 to 0:")
for i in range(10, -1, -1):
    print(i, end=' ')
print("\n\nWhile loop from 10 to 0:")
i = 10
while i >= 0:
    print(i, end=' ')
    i -= 1

# 3. Print triangle
print("\n\n3. Triangle:")
for i in range(1, 8):
    print('#' * i)

# 4. Nested loops to print square
print("\n4. 8x8 Square:")
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

# 5. Print multiplication pattern
print("\n5. Multiplication pattern:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6. Iterate through a list
print("\n6. Loop through list:")
techs = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in techs:
    print(tech)

# 7. Print even numbers from 0 to 100
print("\n7. Even numbers from 0 to 100:")
for i in range(101):
    if i % 2 == 0:
        print(i, end=' ')

# 8. Print odd numbers from 0 to 100
print("\n\n8. Odd numbers from 0 to 100:")
for i in range(101):
    if i % 2 != 0:
        print(i, end=' ')


#NIVEL 2
# 9. Sum of all numbers from 0 to 100
total = 0
for i in range(101):
    total += i
print(f"\n\n9. The sum of all numbers is {total}.")

# 10. Sum of evens and odds
sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"10. The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.")


#NIVEL 3
# 11. Countries containing 'land'
from countries import countries

print("\n11. Countries containing 'land':")
land_countries = [country for country in countries if 'land' in country]
print(land_countries)

# 12. Reverse fruit list using loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])
print("\n12. Reversed fruits:", reversed_fruits)

# 13–15. Using countries_data
from countries_data import countries_data

# 13. Total number of languages
all_languages = []
for country in countries_data:
    all_languages.extend(country['languages'])
unique_languages = set(all_languages)
print("\n13. Total number of unique languages:", len(unique_languages))

# 14. Ten most spoken languages
from collections import Counter
language_counter = Counter(all_languages)
most_spoken = language_counter.most_common(10)
print("14. 10 most spoken languages:")
for lang, count in most_spoken:
    print(f"{lang}: {count}")

# 15. 10 most populated countries
sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)
print("\n15. 10 most populated countries:")
for c in sorted_by_population[:10]:
    print(f"{c['name']}: {c['population']}")
