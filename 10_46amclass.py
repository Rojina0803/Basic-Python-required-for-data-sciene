#Major concept of python required in Data Science
numbers=[1,2,3,4,5]
# squared_numbers=[]
# for numbers in numbers:
#     numbers= numbers*numbers
#     squared_numbers.append(numbers)
#     print(squared_numbers)

#List Comprehension
num_sqrs=[numbers**2 for numbers in numbers]
print(num_sqrs)

# integer=[0,1,3,4,5]
# divided=[integer/2 for integer in integer]
# print(divided)

integer=[0,1,3,4,5]
try:
    divided=[integer/0 for integer in integer]
    print(divided)
except ZeroDivisionError:
    print("Cannot divide by zero.")

#Iterators
fruits=["apple","banana","cherry"]
for f in fruits:
    print(f)
# memory efficient,less time consuming,doesnt occupy large memory space, can acess value one at a time
fruits_it= iter(fruits)
print(next(fruits_it))

CUSTOM ITERATORS

#GENERATORS
#yield works as iterator
def squared_generator(*number):
    for num in number:
        yield num**2
squares=squared_generator(1,2,3,4)
print(next(squares))

#Decorator
#  function that takes function as input
def multiply(a,b):
    return a*b
result= multiply(2,4)
print(result)

def log_function(func):
    def wrapper(a,b):
        result= func(a,b)
        print(f'Parameter are {a} and {b}')
        return result
    return wrapper

@log_function
def multiply(a,b):
    return a*b
result= multiply(2,4)
print(result)

#args,Kargs



#CUSTOM ITERATORS
class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        raise StopIteration

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a custom iterator
iterator = CustomIterator(numbers)

#Iterate over the iterator
for num in iterator:
    print(num)


#CONTEXT MANAGER
with open ('data.txt','r') as file:
    content= file.read()
    print(content)


# LAMDA FUNCTION
def sub_val(x,y):
    return x-y
res= sub_val(3,1)
print(res)

result= lambda x,y: x*2
res= result(4,2)
print(res)


#REGULAR EXPRESSION
import re
text="Nikki was born in 2000-02-23.She is a wonderful person"
pattern=r'\d{4}-\d{2}-\d{2}'
pattern=r'\w*ful'


match= re.search(pattern,text)
if match:
    print(match.group())
    print(match.span())  #slicingg
else:
    print("NO MATCH")

# Write the regular expression for the language containing the string over {0, 1} 
# in which there are at least two occurrences of 1's between any two occurrences of 1's between any two occurrences of 0's.


str="Why Can't You Hold Me In The Dark"
pattern=r'[A-Z]'
match= re.search(pattern, str)
print(match.group())

