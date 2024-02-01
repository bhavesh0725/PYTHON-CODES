#example 1

squares = {x: x**2 for x in range(1, 6)}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)

#example 2
numbers = [1, 2, 3, 4, 5, 6]
parity = {num: 'even' if num % 2 == 0 else 'odd' for num in numbers}
# Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even'}
print(parity)

#example 3
words = ['apple', 'banana', 'orange']
word_lengths = {word: len(word) for word in words}
# Output: {'apple': 5, 'banana': 6, 'orange': 6}

print(word_lengths)

#example 4
words = ['hello', 'world', 'python']
upper_words = {word: word.upper() for word in words}
# Output: {'hello': 'HELLO', 'world': 'WORLD', 'python': 'PYTHON'}
print(upper_words)

#example 5
numbers = [1, 2, 3, 4, 5]
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
# Output: {2: 4, 4: 16}
print(even_squares)

#example 6

keys = ['a', 'b', 'c']
default_values = {key: 0 for key in keys}
# Output: {'a': 0, 'b': 0, 'c': 0}
print(default_values)

#example 7
word = 'programming'
letter_freq = {letter: word.count(letter) for letter in set(word)}
# Output: {'g': 2, 'o': 1, 'r': 2, 'm': 2, 'n': 1, 'i': 1, 'a': 1, 'p': 1}
print(letter_freq)

#example 8

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Wonderland']
info_dict = {keys[i]: values[i] for i in range(len(keys))}
# Output: {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
print(info_dict)

#example 9
numbers = {x: x**2 for x in range(1, 11) if x % 2 != 0}
# Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(numbers)

#example 10

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_dict = {(i, j): matrix[i][j]
                  for i in range(len(matrix)) for j in range(len(matrix[0]))}
# Output: {(0, 0): 1, (0, 1): 2, ..., (2, 2): 9}

print(flattened_dict)
