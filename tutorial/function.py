def fib(n):
    """函数"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

    print()


# Now call the function we just defined
fib(200)

## The default values are evaluated at the point of function definition in the defining scope, so that
i = 5


def f(arg=i):
    print(arg)


i = 6
f()

"""
 Important warning: The default value is evaluated only once.
 This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.
 For example, the following function accumulates the arguments passed to it on subsequent calls:
 默认值居然是累积的，tm就是个巨坑
"""


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

# Keyword Arguments
"""
"""


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print()


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

def cheeseshop(kind, *args, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in args:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkepper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# Arbitrary Argument Lists
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


def concat(*args: list, sep: str = "/"):
    print("annotation:", concat.__annotations__)
    return sep.join(args)


print(concat("earth", "mars", "venus"))

print(concat("earth", "mars", "venus", sep="."))

list(range(3, 6))  # normal call with separate arguments

args = [3, 6]
list(range(*args))  # call with arguments unpacked from a list


# Lambda Expressions
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))

print(f(1))

# Function Annotations
