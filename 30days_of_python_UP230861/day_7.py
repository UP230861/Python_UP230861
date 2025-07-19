# 1. Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("1. Length of it_companies:", len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("2. Added 'Twitter':", it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Intel', 'HP', 'Dell'])
print("3. Added multiple companies:", it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('HP')
print("4. Removed 'HP':", it_companies)

# 5. What is the difference between remove and discard
# Explanation as comment
"""
remove() → lanza un error si el elemento no existe en el set.
discard() → no lanza error si el elemento no existe.
"""
print("5. 'remove' lanza error si no existe, 'discard' no.")

#nivel 2
# 6. Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 23, 25, 28}
joined_AB = A.union(B)
print("6. Join A and B:", joined_AB)

# 7. Find A intersection B
intersection_AB = A.intersection(B)
print("7. A ∩ B:", intersection_AB)

# 8. Is A subset of B
print("8. Is A a subset of B?", A.issubset(B))

# 9. Are A and B disjoint sets
print("9. Are A and B disjoint?", A.isdisjoint(B))

# 10. Join A with B and B with A
A_update = A.copy()
B_update = B.copy()
A_update.update(B)
B_update.update(A)
print("10. A updated with B:", A_update)
print("    B updated with A:", B_update)

# 11. What is the symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print("11. Symmetric difference A ⊕ B:", sym_diff)

# 12. Delete the sets completely
del A
del B
print("12. A and B deleted.")


#nivel 3
# 13. Convert the ages to a set and compare the length of the list and the set
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)
print("13. Length of list:", len(ages))
print("    Length of set:", len(ages_set))
print("    Set has fewer items because it removes duplicates.")

# 14. Explain the difference between string, list, tuple and set
"""
String: Secuencia inmutable de caracteres. Ej: "Hola"
List: Colección ordenada y mutable. Permite duplicados. Ej: [1, 2, 3]
Tuple: Colección ordenada e inmutable. Permite duplicados. Ej: (1, 2, 3)
Set: Colección no ordenada y mutable. No permite duplicados. Ej: {1, 2, 3}
"""
print("14. Tipos de datos explicados en comentarios.")

# 15. Unique words in a sentence using split and set
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("15. Unique words used:", unique_words)
print("    Number of unique words:", len(unique_words))
