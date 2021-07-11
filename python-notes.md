# Python

## Modules
* Python code put in `*.py` files called "modules"
* Directly executed with `python module.py` command
* Bring into the REPL or other modules with `import module` syntax, or `import func from module`, or `import func from module as myfun` syntax
* Defining functions: `def function_name(arg1, argn):`
* using `return` without parameter or omitting it altogether returns `None`
* Use `__name__` to determine how module is used
* Use `if __name__ == __main__` to have flexibility to import or invoke directly
* Module executed exactly once when first imported
* Use `sys.argv` to get command line arguments - `sys.argv[0]` is the script filename
* Docstrings are standalone strings in the first statement of a module or function, delimited by triple quotes:

```python
""" This is a description of the module
"""

import sys

def myfunc():
  """this is my function
  """
```

* Use `help()` function to get module/function documentation
* Use `#` for comments
* Shebang (`#!/usr/bin/env python3`) allows execution as a standalone executable (no need to invoke `python` command first)

## Primitives

* Integers
  * arbitrary precision integral values
* Floats
  * 64-bit floating point decimal values
* Strings
  * List of characters (however, there is no 'character' primitive in python), can be iterated over directly
* Booleans
  * can be `True` or `False`

## Objects

* `id()` returns a unique id for an object
* the `is` operator checks the identity of an object
* variables are named references to objects, as shown below

```python
>>> a = [2,4,6]
>>> b = a
>>> b[1] = 17
>>> a
[2, 17, 6]
>>> b
[2, 17, 6]
>>> a is b
True
```

* Python thus is **pass by reference, not value**

```python
>>> p = [1, 3, 5]
>>> q = [1, 3, 5]
>>> p == q
True
>>> p is q
False
```

* *value equality* is different from *identity*
* Default arugments for functions can be specified (must come after args without defaults): `def myfunc(a, b=value):`
* Default argument values are evaluated when `def` is evaluated
  * No problem when default is immutable constant like integer or string
  * But can be tricky if using mutable objects like collections as defaults - so **ONLY USE IMMUTABLE OBJECTS AS DEFAULTS**
* Python is **dynamically typed** - object types are resolved at runtime
* However, Python is also **strongly typed** - type coercion is not allowed!

```python
def add(a, b): # types not defined here! can accept any type where + operator is defined
    return a + b

add(1,2) # 3
add(3.1, 2.4) #5.5
add("news","paper") #newspaper
add([1,6],[21,107]) # [1, 6, 21, 107]
# but this is NOT allowed..
add("the answer is ", 42) # TypeError: can't convert int to str implicitly
```

### Scopes
* Scopes are contexts in which references can be looked up. 4 scopes:
  * Local - inside the current function
  * Enclosing - Any and all enclosing functions
  * Global - top-level of module
  * Built-in - provided by `builtins` module
* LEGB rule - look for variables in up the scope chain
* Variable shadowing can occur, use the `global` keyword to prevent this and refer to global variable
* In Python, *everything* is an object
* Use `type()` function to see type of an object
* Use `dir()` function to see sorted list of module attributes, including default, defined, and imported names

## Collections

### Tuples
* Immutable sequence of arbitrary objects
* example: `t = ("andrew", 24)`
* Access via 0-based index in square brackets: `t[0] == "andrew"`
* `len()` returns number of elements
* can iterate over with `for` loop, and concatenate with `+` operator
* repeat with `*` operator
* can have nested tuples - access with repeated indexing in brackets: `tuple[i][j]`
* use trailing `,` to specify single element (otherwise would parse as the object itself: `h = (12,)`
* use empty parentheses for empty tuple: `k = ()`
* parentheses of multiple tuples may be omitted: `r = 1, 1, 2, 3, 5, 8`
* tuple unpacking allows destructuring (even with nested tuples)
* variable swapping: `a, b = b, a`

```python
def minmax(items):
    return min(items), max(items)

a, b = minmax([1, 10, 15, -5, 60])
print(a) # -5
print(b) # 60
```
* use tuple constructor to define from a list: `tuple([1, 4, 9, 16])` or a string: `tuple("hello") # ('h','e','l','l','o')`
* `in` and `not in` operators check membership in a tuple (and other collections)

### Strings
* Homogeneous sequence of Unicode codepoints
* Use `len` to return length of a string
* Use `+` and `+=` operator for concatenation, but `.join()` method for more efficient performance: `names = ','.join(['andrew','blake','seth'])`
* `.split()` method is the opposite of `.join()`
* `.partition()` method breaks string into 3 parts around a separator: `'abcde'.partition('cd') # ('ab', 'cd', 'e')`
  * Underscore variable conventionally used when unpacking unwanted element from tuple: `depart, _, arrive = 'Vegas:DC'.partition(':')`
* Use `.format()` with "replacement fields" delimited by `{}`: `"the age of {0} is {1}".format('Andrew',24)`
```python
import math
"Math constants: pi={m.pi}, e={m.e}".format(m=math)
"Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math) #formatted to 3 decimal places
```

### Range
* Arithmetic progression of integers

```python
for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4
```
* Use `.enumerate()` for counters
```python
for i, v in enumerate(t):
    print("i = {}, v = {}".format(i,v))
```

### List
* heterogeneous mutable sequence
* 0-based index
* append with `.append()`
* negative integers index from the end (negative indexing is 1-based instead of 0-based)
* slicing lets us extract part of a list: `slice = seq[start:stop]`
  * omitting the "stop" element slices to the end, omitting "start" slices from the beginning
  * copy a list by omitting both "start" and "stop": `a = b[:]`
  * can also copy with `.copy()` method or using `list()` constructor
  * copies are shallow
* repeat lists with the `*` operator
  * use for initializing constant value list: `s = [3] * 30 # s is a list of size 30, all values are 3`
  * repetition is shallow
* `.index()` returns the index of the given value in the list: `[1, 3, 5 ,7].index(5) == 2`
* count occurances with `.count()`
* remove elements with `del` keyword: `del s[1]`
* or remove by value: `s.remove("entry")`
* use `.insert()` to put a value in at the specified index: `s.insert(2, "hello")`
* `.extend()` is the same as `+=`
* `.reverse()` and `.sort()` methods useful
  * `.sort()` accepts a "key" function and a "reverse" boolean
* `.sorted()` built-in function sorts an iterable and returns a list: `y = sorted(x)`
* `.reversed()` is similar to `.sorted()`, but returns an iterator - use `list()` constructor on the result: `q = list(reversed(p))`

### Dictionaries
* key-value pairs
* lookup by key
* keys must be immutable - lists not allowed, but strings, tuples, and numbers are
* values can be mutable
* order of dict may vary, not reliable
* `dict()` constructor accepts:
  * 2-tuples with iterable series of key-values
  * keyword arguments
  * a mapping, such as another dict
* use constructor or `.copy()` for copying
* Extend dictionary with `.update()`
* Use `.values()` to get an iterable of values: `for value in colors.values():`
* Get keys, values at once in iteration: `for key, value in colors.items():`
* `in` and `not in` operators work on the *keys*

### Sets
* Unordered collection of unique, immutable objects
* `{}` makes a `dict`, so use `set()` constructor to create a set
* Iterable, but order is arbitrary
* `.add()` adds an element, does nothing if already exists in the set
  * for multiple elements, use `.update()`
* use `.remove()` to remove elements from the set
  * if the element doesn't exist in the set, a `KeyError` is thrown
* Set algebra
  * `s.union(t)` method returns a set by performing UNION operation (returns elements which exist in either set)
  * `s.intersection(t)` method finds and returns elements within BOTH sets
  * `s.difference(t)` method returns elements in the first set which are NOT in the second (non-commutative)
  * `s.symmetricdifference(t)` method returns elements which the sets do NOT share in common
  * `s.issubset(t)` checks whether `s` is a subset of `t`
  * `s.issuperset(t)` checks the inverse - whether `s` is a superset of `t`
  * `s.isdisjoint(t)` checks whether the two sets have no members in common

### Collection Protocols
| Protocol  | Implementing Collections
| ----------|--------------------------|
| Container | str, list, range, tuple, bytes, set, dict
| Sized     | str, list, range, tuple, bytes, set, dict
| Iterable  | str, list, range, tuple, bytes, set, dict
| Sequence  | str, list, range, tuple, bytes
| Mutable Sequence | list
| Mutable Set      | set
| Mutable Mapping  | dict

* **Container**: membership testing using `in` and `not in`
* **Sized**: can determine number of elements with `len()`
* **Iterable**: can produce an *iterator* with `iter(s)`, able to use `for` loop
* **Sequence**: can retrieve elements by index, find items by value, count items, and produce a reversed sequence
* **Mutable Sequence**:
* **Mutable Set**:
* **Mutable Mapping**:

## Exceptions
* **Raise** an exception to interrupt program flow
* **Handle** an exception to resume control
* Unhandled exceptions will terminate the program
* use `try/except` blocks to catch Errors
  * multiple `except` handlers for different `Errors` allowed
  * can use tuple to handle multiple errors in one block
  * since a block without a statement is not allowed, the `pass` keyword can be used which does nothing
  * use `as` clause to get a reference to the exception
  * use `raise` to re-raise the exception/error caught
* Common errors:
  * `IndexError`: when an index is out of range
  * `KeyError`: when lookup in a mapping fails
  * `ValueError`: object is right type but has inappropriate value
  * `TypeError`: object is the wrong type
    * avoid protecting against this error
* Exceptions require explicit handling, Errors are silent by default
* `try/finally` lets you clean up whether or not exception occurs

## Comprehensions
* Concise syntax for describing lists, sets, and dictionaries
* Declarative, functional, readable, and expressive

```python
# list comprehension
words = "Why sometimes I believed as many as six impossible things before breakfast".split()
[len(word) for word in words]
# [3, 9, 1, 4, 8, 2, 4, 2, 3, 10, 6, 6, 9]
# set comprehension
{len(word) for word in words}
# [1, 2, 3, 4, 6, 8, 9, 10]
```

```python
from pprint import pprint as pp
country_to_capital = {'United Kingdom': 'London', 'Brazil': 'Brazilia', 'Morocco': 'Rabat'}
# dict comprehension
country_to_capital = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)
# duplicates: later keys override earlier
```

* Comprehensions have optional "if" clause with a predicate: `[expr(item) for item in items if predicate(item)]`

## Iterables
* Can pass an iterable to the `iter(i)` function
* Can pass iterator to the `next(i)` function

```python
iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
next(iterator) # 'Spring'
next(iterator) # 'Summer'
```

## Generators
* Specify iterable sequences (**all Generators are Iterators**)
* Lazily evaluated
  * Next value evaluated on-demand
* Can model infinite sequences (like streams)
* Composable into pipelines for natural stream processing
* Defined as **any function which uses the `yield` keyword at least once**

```python
def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()
g # <generator object gen123 at 0x100.....>
next(g) # 1
next(g) # 2
next(g) # 3
next(g) # StopIteration exception
```

### Stateful Generators
* Generators can maintain state with local variables

```python
def take(count, iterable):
    "Take first count elements"
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item
```

* Generator expressions are a cross between generator functions and comprehensions
* Syntax similar to list comprehensions: `(expr(item) for item in iterable)`

```python
million_squares = (x*x for x in range(1,1000001))
# remember, lazy execution! no squares have been calculated yet
list(million_squares) # produces a long....... list
# generators are one time use only
list(million_squares) # []

sum(x*x for x in range(10000001))
# produces big number
# if we did this with list comprehension, it'd take ~400MB of memory
# with generators, memory usage is insignificant due to lazy execution
```

### Itertools Module
* Common tools: islice, chain, count
* Built-ins: sum, any, all, zip, min, max, enumerate

```python
import itertools import chain
sunday = [1, 3, 5, 7, 9, 10, 15]
monday = [2, 4, 6, 8, 12, 24, 48]
for item in zip(sunday, monday):
    print(item)

# (1,2)
# (3,4)
# (5,6)
# etc...

temperatures = chain(sunday, monday)
all(t > 0 for t in temperatures)
# True
```

## Classes
* Python lets you solve simple problems without classes, but when needed you can create classes to solve complex problems
* Object-oriented without forcing you to deal with classes until you need them
* Class names are CamelCase by convention
* Call the constructor with the class name followed by parentheses: `Class()`
* `self` is the first argument to all **instance** methods
* `__init__(self)` method defines behavior for initializing new objects
  * **NOT a constructor**, just an initializer
  * `self` is similar to `this` in C++ or Java
  * **Class invariants** enforced here - should persist for the lifetime of the class

```python
'''Model for aircraft flights'''
class Flight:

    def __init__(self, number):
      # _number avoids name clash with argument (also, it's convention)
        self._number = number # assignment to attribute that doesn't exist creates one

    def number(self):
        return self._number
```

* Python uses **duck typing** - suitability for polymorphism is determined at runtime based on attributes the object has
* Inheritance is mostly useful for sharing implementations
  * Specify the base class in parentheses - `class AirbusA319(Aircraft):`

## Files and Resources
* Open a file: use built-in `.open(file, mode, encoding)`
* Two modes: binary and text
  * Binary: read / write in bytes
  * Text: support for universal newline (`\n`)
  * all possible mode flags: 'r', 'w', 'x', 'a', 'b', 't', '+', 'U'
* use `.read()` and `.write()` methods to read/write bytes & characters
* use `.seek()` to move file pointer position
* use `.readline()` to read line-by-line, while `.readlines()` reads all lines in the file to a list
* use `.close()` to close the file - **required to actually write the data to file**
* Files as iterators: `for line in file:`
* Use `with-block` with any *context manager* for resource cleanup: `with open(filename, mode='rt', encoding='utf-8') as f:`
  * `.close()` no longer necessary!
* file-like objects have loosely defined behaviors - if it looks like a file and acts like a file, it's a file

```python
from urllib.request import urlopen
with urlopen('http://www.sixty-north.com/c/t.txt') as web_file:
    for line in web_file:
        print(line)
```

## Testing
* `unittest` module:
* TestCase groups together related test functions
* *fixtures* run before and/or after each test method
* Extend the `unittest.TestCase`, and define test methods starting with `test_` - this will be auto-registered by the unittest module

```python
import unittest

def mymethod:
  pass

class TextAnalysisText(unittest.TestCase):

  def setUp(self):
    """runs before the test"""
    pass

  def tearDown(self):
    """runs after the test"""
    pass

  def test_function_runs(self):
    """Basic test"""
    mymethod()
    self.assertEquals(1,1)

if __name__ == __main__:
  unittest.main()
```

* `pbb` module
* can import as normal, e.g. on the REPL: `import pdb`, then use `pdb.set_trace()` to start debugging
* or when running a script: `python3 -m pdb script.py`
* use `help` command to list `pdb` commands available
* `pdb` shows the next statement that will be run
* useful commands: `next`, `cont`, `list`, `return`, `quit`, `where`, `print`

## Virtual Environment
* `python3 -m venv env_name`
