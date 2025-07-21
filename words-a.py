list_a = ["apple", "banana", "carrot", "black", "box"] # List A for testing
list_b = []
for word in list_a:
    if word.startswith('b'):
        list_b.append(word.capitalize())
print(list_b)