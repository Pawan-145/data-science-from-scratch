# Linear Algebra
# Vectors
from typing import List
#Vectors only Add they are of same length
Vector = List[float]
height_weight_age = [70,170,40]

# Vector Addition

def add(v:Vector, w:Vector)-> Vector:
    assert len(v)==len(w), "Vectors must be in same length"
    return[v_i+w_i for v_i,w_i in zip(v,w)]
assert add([1,2,3],[2,3,4]) == [3,5,8]

# Vector Subtraction
def subtract(v:Vector,w:Vector):
    assert len(v) == len(w)
    return[v_i-w_i for v_i, w_i in zip(v,w)]

assert subtract([5,7,9],[4,5,6]) == [1,2,3]

# Addition of Vectors without knowing number of vectors
def vector_sum(vectors: List[Vector]) -> Vector:
    # check that vectors is not empty
    assert vectors, "no vectors provided!"

    # check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes"
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

assert vector_sum([[1,2],[3,4],[5,6],[7,8]]) == [16,20]

# Vector Multiplication
def scalar_multiplication(c:float,v:Vector)-> Vector:
    return[c*v_i for v_i in v]

assert scalar_multiplication(2,[1,2,3]) == [2,4,6]

# Componentwise means of list of(same-sized)vectors:
def vector_mean(vectors: List[Vector])-> Vector:
    num_elements = len(vectors)
    return [(1/num_elements)*i for i in vector_sum(vectors)]



# Vector dot-Product, dot-product is for only two vector
def dot(v:Vector,w:Vector)->Vector:
    assert len(v) == len(w), "vectors must be of same length"
    return sum(v_i*w_i for v_i,w_i in zip(v,w))



#  Multiplies the i-th elements of all vectors together, then sums over all positions
def product(values):
     result = 1
     for x in values:
         result *= x 
     return result

def sum_of_elementwise_products(vectors:list[Vector])-> float:
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes"
    return sum([product(vector[i] for vector in vectors) for i in range(num_elements)])

# Vector's sum of squares
def sum_of_squares(v:Vector)->float:
    return dot(v,v)

assert sum_of_squares([1,2,3]) == 14

# Magnitude
import math
def magnitude(v:Vector)->float:
    return math.sqrt(sum_of_squares(v))

assert magnitude([3,4]) == 5 

# Distance between two vectors
def squared_distance(v:Vector, w:Vector) -> float:
    return sum_of_squares(subtract(v,w))

def distance(v:Vector, w:Vector) -> float:
    return math.sqrt(squared_distance(v,w))

# this is equivalent as if we write
def distance(v:Vector,w:Vector) -> float:
    return magnitude(subtract(v,w))

# Matrices
Matrix  = list[List[float]]
A = [[1,2,3]
     [4,5,6]]
B = [[1,2],
     [3,4],
     [5,6]]

# for rows in matrix A use len(A)
# for columns in matrix A use use len(A[0])
from typing import Tuple
def shape(A:Matrix)-> Tuple[int,int]:
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows,num_cols

assert shape([[1,2,3],[4,5,6]])== (2,3)           # 2 rows, 3 columns

def get_row(A:Matrix, i:int)-> Vector:
    return A[i]          # A[i] is already the ith row

def get_column(A:Matrix,j:int)->Vector:
    return[A_j[j]                               #jth element of row A_i
           for A_j in A]                        #for each row A_i

from typing import Callable
def make_matrix(num_row:int,
                num_col:int,
                entry_fn: Callable[[int,int], float])-> Matrix:
    return[[entry_fn(i,j)
           for j in range(num_col)]
           for i in range(num_row)]

# Identity matrix
def identity_matrix(n:int)->Matrix:
    return make_matrix(n,n,lambda i,j:1 if i == j else 0)

assert identity_matrix(5) == [[1,0,0,0,0],
                              [0,1,0,0,0],
                              [0,0,1,0,0],
                              [0,0,0,1,0],
                              [0,0,0,0,1]]

friends_of_five = [i
                   for i, is_friend in enumerate(identity_matrix(5))
                   if is_friend]
