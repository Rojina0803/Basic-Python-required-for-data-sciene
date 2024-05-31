# #Major concept of python required in Data Science
# numbers=[1,2,3,4,5]
# # squared_numbers=[]
# # for numbers in numbers:
# #     numbers= numbers*numbers
# #     squared_numbers.append(numbers)
# #     print(squared_numbers)

# #List Comprehension
# num_sqrs=[numbers**2 for numbers in numbers]
# print(num_sqrs)

# # integer=[0,1,3,4,5]
# # divided=[integer/2 for integer in integer]
# # print(divided)

# integer=[0,1,3,4,5]
# try:
#     divided=[integer/0 for integer in integer]
#     print(divided)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# #Iterators
# fruits=["apple","banana","cherry"]
# for f in fruits:
#     print(f)
# # memory efficient,less time consuming,doesnt occupy large memory space, can acess value one at a time
# fruits_it= iter(fruits)
# print(next(fruits_it))

#CUSTOM ITERATORS

# #GENERATORS
# #yield works as iterator
# def squared_generator(*number):
#     for num in number:
#         yield num**2
# squares=squared_generator(1,2,3,4)
# print(next(squares))

# #Decorator
# #  function that takes function as input
# def multiply(a,b):
#     return a*b
# result= multiply(2,4)
# print(result)

# def log_function(func):
#     def wrapper(a,b):
#         result= func(a,b)
#         print(f'Parameter are {a} and {b}')
#         return result
#     return wrapper

# @log_function
# def multiply(a,b):
#     return a*b
# result= multiply(2,4)
# print(result)

# #args,Kargs



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


#CONTEXT MANAGERS

class Open_file():
    def __init__(self,filename,mode) :
        self.filename= filename
        self.mode= mode

    def __enter__(self):
        self.file =open(self.filename,self.mode)
        return self.file
    
    def __exit__(self,exc_type,exc_val,traceback):
        self.file.close()

with Open_file('Sample.txt','w') as f:
    f.write('Testing')

print(f.closed)


# LAMDA FUNCTION

def double(x):
    return x*2
print(double(5))

def grave(fx,value):
    return 6* fx(value)

double= lambda x:x*2
print(double(5))

cube = lambda x,y,z:(x+y+z)/3
print(cube(6,7,8))

print(grave(lambda x:x*x*x,2))



#REGULAR EXPRESSION

import re

text = "The quick brown fox jumps over the lazy dog. The dog is sleeping."
pattern = r"\bdog\b"

matches = re.findall(pattern, text)
print("Matches found:", matches)

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
x = re.search("Portugal", txt)
print(x)