d4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}

d7 = {a: b for a, b in d6.items() if a not in d5}
print(d7)
