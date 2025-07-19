# 1. Create an empty tuple
empty_tuple = ()
print("1. Empty tuple:", empty_tuple)

# 2. Create a tuple containing names of your sisters and your brothers
sisters = ('Anna', 'Maria')
brothers = ('John', 'James')
print("2. Sisters:", sisters)
print("   Brothers:", brothers)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print("3. Siblings:", siblings)

# 4. How many siblings do you have?
print("4. Number of siblings:", len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Father', 'Mother')
print("5. Family members:", family_members)

#NIVEL 2
# 6. Unpack siblings and parents from family_members
*unpacked_siblings, father, mother = family_members
print("6. Unpacked siblings:", unpacked_siblings)
print("   Father:", father)
print("   Mother:", mother)

# 7. Create fruits, vegetables and animal products tuples
fruits = ('apple', 'banana', 'mango')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'egg', 'meat')
print("7. Fruits:", fruits)
print("   Vegetables:", vegetables)
print("   Animal Products:", animal_products)

# 8. Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print("8. Food stuff (tuple):", food_stuff_tp)

# 9. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("9. Food stuff (list):", food_stuff_lt)

# 10. Slice out the middle item or items
length = len(food_stuff_lt)
middle = length // 2
if length % 2 == 0:
    middle_items = food_stuff_lt[middle-1:middle+1]
else:
    middle_items = [food_stuff_lt[middle]]
print("10. Middle item(s):", middle_items)

# 11. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("11. First three items:", first_three)
print("    Last three items:", last_three)

# 12. Delete the food_stuff_tp tuple completely
del food_stuff_tp
print("12. food_stuff_tp deleted.")

# 13. Check if an item exists in tuple: 'Estonia' in nordic_countries
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("13. Is 'Estonia' a Nordic country?", 'Estonia' in nordic_countries)

# 14. Check if 'Iceland' is a nordic country
print("14. Is 'Iceland' a Nordic country?", 'Iceland' in nordic_countries)
