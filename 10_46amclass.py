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
