# 1. Six digit/character random_user_id
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(random_user_id())  # Example: '1ee33d'

# 2. user_id_gen_by_user
def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters: "))
    num_ids = int(input("Enter number of IDs: "))
    for _ in range(num_ids):
        print(''.join(random.choices(string.ascii_letters + string.digits, k=num_chars)))

# user_id_gen_by_user()  # Example input: 5 5

# 3. rgb_color_gen
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())  # Example: rgb(125,244,255)

#NIVEL_2
# 4. list_of_hexa_colors
def list_of_hexa_colors(n):
    colors = []
    for _ in range(n):
        hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(hex_color)
    return colors

print(list_of_hexa_colors(3))  # Example: ['#a3e12f','#03ed55','#eb3d2b']

# 5. list_of_rgb_colors
def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

print(list_of_rgb_colors(3))  # Example: ['rgb(12,45,78)', 'rgb(255,22,99)', 'rgb(0,0,0)']

# 6. generate_colors
def generate_colors(type, num):
    if type == 'hexa':
        return list_of_hexa_colors(num)
    elif type == 'rgb':
        return list_of_rgb_colors(num)
    else:
        return "Invalid type. Use 'hexa' or 'rgb'."

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 2))

#NIVEL 3
# 7. shuffle_list
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

print(shuffle_list([1, 2, 3, 4, 5]))  # Example: [3, 5, 1, 2, 4]

# 8. Seven unique random numbers from 0 to 9
def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())  # Example: [4, 1, 6, 0, 9, 2, 5]
