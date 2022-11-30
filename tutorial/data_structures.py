from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")  # Terry arrives
print(queue)
queue.append("Graham")  # Graham arrives
print(queue)
queue.popleft()  # The first to arrive now leaves
print(queue)

queue.popleft()  # The second to arrive now leaves
print(queue)

queue  # Remaining queue in order of arrival

squares = [x ** 2 for x in range(10)]
print(squares)
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x * 2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# apply a function to all the elements
print([abs(x) for x in vec])

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
print([(x, x ** 2) for x in range(6)])

# the tuple must be parenthesized, otherwise an error is raised
# print([x, x ** 2 for x in range(6)])

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

# Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print("matrix", matrix)

print("[[row[i] for row in matrix] for i in range(4)]", [[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print("transposed", transposed)

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print("transposed", transposed)

print("list(zip(*matrix))", list(zip(*matrix)))

# set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed

print("'orange' in basket", 'orange' in basket)  # fast membership testing

print("'crabgrass' in basket", 'crabgrass' in basket)

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print("a", a, sep='=')  # unique letters in a
print("b", b, sep='=')  # unique letters in b

print("a - b", a - b, sep='=')  # letters in a but not in b

print("a | b", a | b, sep='=')  # letters in a or b or both

print("a & b", a & b, sep='=')  # letters in both a and b

print("a ^ b", a ^ b, sep='=')  # letters in a or b but not both

# Map
tel = {'jack': 4098, 'sape': 4139}
print("tel=", tel)
print("dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])", dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print("dict(sape=4139, guido=4127, jack=4098)", dict(sape=4139, guido=4127, jack=4098))
print("{x: x**2 for x in (2, 4, 6)}", {x: x**2 for x in (2, 4, 6)});
