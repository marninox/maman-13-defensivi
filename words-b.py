list_a = ["apple", "banana", "carrot", "black", "box"] # List A for testing

# One liner to solve the problem
list_b = [word.capitalize() for word in list_a if word.startswith('b')]

print(list_b)