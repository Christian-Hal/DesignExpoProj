# using the filter function examples
# method 1
def funFilter(number):
    if number >= 100 and number % 5 == 0:
        return number
theList = list(filter(funFilter, range(100, 501)))

# method 2
numList = list(filter(lambda number: number >= 100 and number % 5 == 0, range(100, 501)))


# using the map function to maipulate a list
# method 1
def fact(n):
    prod = 1
    while n > 0:
        prod *= n
        n -= 1
    return prod

nums = list(map(fact, range(11)))


# method 2
mapList = list(map(lambda number: number * 2, [1,2,3,4,5,6,7,8,9,10]))


# using the reduce funtion example
from functools import reduce
list8 = [1,2,3,4,5,6,7,8,9]
reduceList = reduce(lambda x, y: x + y, list8)


# using list comprehension to construct a list of of only even values from 0-10 including 10
evenList = [x for x in range(11) if x % 2 == 0]
oddList = [x for x in range(101) if x % 2 != 0 and x >= 50]


# dictionary practice
practice = {1:"value", "key":"value"}
dc = { num :  { num * 2  : num * 3 }  for num in range(10)}
print(dc)
