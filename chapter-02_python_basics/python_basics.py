"""
Chapter 2 - Python Basics for Data Science
Author: Pawan Kumar Ray
Book: Data Science from Scratch - Joel Grus

This file contains practice code covering:
- Python syntax
- Data structures
- Functions
- OOP
- Generators
- Randomness
- Type hints
"""

# Concept of Indentation 
for i in [1,2,3,4,5]:
    print(i)                 # first line in "for i" block
    for j in [1,2,3,4,5]:
        print(j)             #first line in "for j" block
        print(i+j)           #last line "for j" block
    print(i)                 # last line in "for i" block

#modules
import re                     #targeting whole module as original name
res  = re.compile()
#Also to use any function of module here 're' , use re.function()

import re as regex              # Using 're' module as 'regex'

# to import specific functions
from collections import defaultdict, Counter

#functions
def double(x):
    return x*2

def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double)

# Using Lambda
y = apply_to_one(lambda x:x+4)

#store lambda in variable
another_double = lambda x: 2*x      # It's fine but don't do this 

def another_double(x):           # Do this instead of this 
    return 2*x

# Strings  (Writing only important parts)
first_name = "Steve"
last_name = "Rogers"

print(f"{first_name} {last_name}")

# Exceptions
try:
    print(0/0)
except ZeroDivisionError:
    print("cannot divide by zero")

#Lists (Writing only important parts)
_, y = [1,2]
x,y = y,x

#Tuples (Writing only important parts)
x,y = y,x   # Pythonic way to swap variables

#Dictionaries (writing only important parts)

grades = {"joel":80, "Tim":95}

joels_grade = grades.get("joel",0)
no_ones_grade = grades.get("no one")
kates_grade = grades.get("Kate",0)


#There is 3 approaches to write same code for identifying present element and if not then adding it in terms of count

# 1st approach
word_count = {}
for word in document:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1          

# 2nd approach
word_count = {}
for word in document:
 try:
    word_count[word] +=1
 except:
    word_count[word] = 1

# 3rd approach

word_count = {}
for word in document:
 previous_count = word_count.get("word",0)
 word_count[word] = previous_count + 1 

# DefaultDict
from collections import defaultdict

words_counts = defaultdict(int)
for word in document:
   word_counts[word] +=1

dd_list = defaultdict(list)
dd_list[2].append(1)

dd_dict = defaultdict(dict)
dd_dict["joel"]["City"] = "Seattle"

dd_pair = defaultdict(lambda: [0,0])
dd_pair[2][1] = 1 

#useful to count wins and losses
scores = defaultdict(lambda: [0, 0])

scores["Alice"][0] += 1   # wins
scores["Alice"][1] += 1   # losses

# Counter 
# A counter instance has a most_common method that is frequently useful:\
from collections import Counter
for word, count in word_counts.most_common(10):
   print(word,count)

# Sets 
# In Sets "in" operation run faster than list
s = set()         # for empty set use set() 
s.add(1)
s.add(2)

stopwords_list = ["a","an","at"] + hundreads_of_words + ["yet","you"]

zip in stopwords_list    #False, but have to check every element

stopwords_set = set(stopwords_list)
"zip" in stopwords_set   #very fast to check

# Control flow (if-else if-else)
if i>2:
   print("greateer then 2")
else:
   print("smaller than 2")

# Ternary operator
res = "even" if x % 2==0 else "odd" 

 # little complex logic 
for x in range(10):
   if x == 3:
      continue
   if x == 5:
      break
   print(x)      # output = 0, 1, 2, 4

# Truthiness
s = some_function_that_returns_string()
if s:
   first_char = s[0]
else:
   first_char = ""

 # shorter way but more confusing using "AND"
first_char = s and s[0]

 # Using "or"
safe_x = x if x is not None else 0

all([])  #True , no falsy statement in the list
any([])  #False, no truthy element in the list

# Sorting
x = sorted([1,2,-3,4,-5],key=abs, reverse=True)

wc = sorted(words_dict.items(),key=lambda counts:counts[1], reverse=True)

# List Comprehensions

increasing_pairs = [
   (x,y)
   for x in range(10)
   for y in range(x+1,10)
]

# Automated Testing and Assert

def smallest_item(xs):
   return min(xs)

assert smallest_item([10,20,5,40]) == 5
assert smallest_item([1,0,-1,2]) == -1

def smallest_item(xs):
   assert xs, "empty list has no smallest team"
   return min(xs)

# OOP (Object Oriented Programming)
class CountingClicker:
   def __init__(self,count=0):
      self.count = count
## In OOP __repr__ , which produces string representation of class inheritance
   def __repr__(self):
    return (f"CountingClicker(count={self.count})")
   def click(self,num_time = 1):
      self.count += num_time
   def read(self):
      return self.count
   def reset(self):
      self.count = 0

clicker1 = CountingClicker()    # Initialized with 0
clicker2 = CountingClicker(100)  # start with count = 100
clicker3 = CountingClicker (count=100)    # more explicit way of doing the same

clicker  = CountingClicker()
clicker.read()
assert clicker.read() == 0
clicker.click()
clicker.reset()
assert clicker.read() == 0

class NoResetClicker(CountingClicker):
   def reset(self):
      pass

clicker4 = NoResetClicker()
clicker4.read()
clicker4.reset()
clicker4.click()

# Iterable and Generator

def generate_range(n):
   i = 0
   while i < n:
      yield i      #Every call to yield produces a value of the generator
      i += 1

names = ["Alice","Bob","Golduck","Heron"]

for i , name in enumerate(names):
   print(f"name{i} is {name}")

# Randomness
import random 
random.seed(10)

for_uniform_randomness = [random.random() for _ in range(4)]    #random.random() produces number uniformly between 0 and 1

# for range
random.randrange(3,6)

# for shuffle
u = [1,2,3,4,5]
random.shuffle(u)

# Random choice
my_bff = random.choice(["steve","hulk","Robert"])

# Choosing sample of elements without duplicate
lottery = range(60)
winning = random.sample(lottery,6)

# To choose sample of elements with duplicates or replacement just make multiple calls to random.choice()

four_random = ([random.choice(range(10)) for _ in range(4)])

# Regular Expressions
import re
re_examples = [
   not re.match("a","cat"),
   re.search("a","cat"),
   not re.search("c","dog"),
   3 == len(re.split("[ab]","carbs")),
   "R-D-" == re.sub("[0-9]","-","R2D2")
]

# Zip and Argument Unpacking
list1 = ['a','b','c']
list2 = [1,2,3]
zip_list = [pair for pair in zip(list1,list2)]
 
# If  lists are of different lengths, zip stops as soon as first list ends.

# Unzip
pairs = [('a',1),('b',2),('c',3)]
letters,numbers = zip(*pairs)
# Another way
letters,numbers = zip(('a',1),('b',2),('c',3))

# Argument unpacking with any function
def add(a,b):
   return (a+b)

add (1,2)
try:
   add([1,2])
except:
   print("add expects two inputs")

add(*[1,2])

# Args and Kwargs
# *args = positional arguments
# **kwargs = keyword argumnets

def magic(*args,**kwargs):
   print("unnamed args: ",args)
   print("keyword args: ",kwargs)

magic(1,2,key="word",key2="word2")

def other_way_magic(x,y,z):
   return x+y+z

x_y_list = [1,2]
z_dict = {"z":3}

print(other_way_magic(*x_y_list,**z_dict))
assert (other_way_magic(*x_y_list,**z_dict)) == 6

def double_check(f):
   def g(*args,**kwargs):
      return 2*f(*args,**kwargs)   
   return g

def f1(x,y):
   return x+y   
g  = double_check(f1)
g(3,5)


# Type Annotations
def total(xs:list)->float:
   return sum(xs)

 # tying module provide number of parameterized types
from typing import List       # note capital L
def total(xs: List[float])->float:
   return sum(total)

# Python 3.9+ allows the simpler form:
def total(xs: list[float]) -> float:
    return sum(xs)

# Optional
from typing import Optional
values: list[int] = []
best: Optional[float] = None                     # This allows either to be float or None

# Alternative for optional in pyton 3.10+ version
best: float | None = None   # Python 3.10+


from typing import Dict,Iteralble,Tuple
count: Dict[str,int] = {'data':1, "science":2}
 
 # lists and generators are both iterable
if lazy:
   evens: Iterable[int] = (x for x in range(10) if x%2==0) 
else:
   evens = [0,2,4,6,8]

# callable
from typing import Callable
# the type hint says that repeater is a function that takes
# two arguments, a string and and an int, and returns a string
def twice(repeater:Callable[[str,int],str], s:str) -> str:
   return repeater(s,2)

def comma_repeater(s:str, n:int)-> str:
   n_copies = [s for _ in range(n)]
   return ','.join(n_copies)

assert twice(comma_repeater,"type hints") == "type hints, type hints"

# As type annotations are just python objects, we can assign them to variables

Number = int
Numbers = List[Number]
def total(xs:Numbers) -> Number:
   return sum(xs)

# __annotations__ 
#  stores type hints (type annotations) for variables, function parameters, and return values.
def add(a: int, b: int) -> int:
    return a + b

print(add.__annotations__)    
# output = {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


