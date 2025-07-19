# 1. Filter only negative and zero
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_and_zero = [n for n in numbers if n <= 0]
print(neg_and_zero)  # [-4, -3, -2, -1, 0]

# 2. Flatten nested list of lists
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = [num for sublist in list_of_lists for inner in sublist for num in inner]
print(flat_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Create list of tuples
tuples_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuples_list)

# 4. Flatten countries to list with uppercase and abbreviations
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_countries = [[country.upper(), country[:3].upper(), city.upper()] for group in countries for (country, city) in group]
print(flat_countries)

# 5. Convert to list of dictionaries
country_dicts = [{'country': country.upper(), 'city': city.upper()} for group in countries for (country, city) in group]
print(country_dicts)

# 6. Convert names list to concatenated full names
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for group in names for (first, last) in group]
print(full_names)  # ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# 7. Lambda function for slope and y-intercept
# Equation form: y = mx + b
# Slope (m) = (y2 - y1) / (x2 - x1)
# y-intercept (b) = y - mx

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
intercept = lambda x, y, m: y - m * x

# Example usage:
m = slope(2, 3, 4, 7)       # Slope between points (2, 3) and (4, 7)
b = intercept(2, 3, m)      # Intercept using one of the points
print("Slope:", m)
print("Y-intercept:", b)
