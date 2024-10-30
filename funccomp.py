#iven an array of functions [f1, f2, f3, ..., fn], return a new function fn that is the function composition of the array of functions.
#The function composition of [f(x), g(x), h(x)] is fn(x) = f(g(h(x))).
#The function composition of an empty list of functions is the identity function f(x) = x.
#You may assume each function in the array accepts one integer as input and returns one integer as output.

from functools import reduce
def compose(functions):
    if not functions:
        return lambda x: x  
    
    return lambda x: reduce(lambda acc, f: f(acc), reversed(functions), x)

    
    return composed
functions = [
    lambda x: x + 1,
    lambda x: x * x,
    lambda x: 2 * x
]
x = 4

composed_fn = compose(functions)
result = composed_fn(x)
print(result) 
