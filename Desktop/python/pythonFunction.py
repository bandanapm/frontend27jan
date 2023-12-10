# define function
def fun1():
    print("I am a function")

# function takes argument
def fun2(arg1, arg2):
    print(arg1," ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# Function with default value for an argument
def power(num, x=1):
    result =1;
    for i in range(x):
        result = result * num
    return result

# Function with variable number of argumnents
def multi_add(*args):
    result =0
    for x in args:
        result = result + x
    return result

# Output
fun1()
fun2(10,20)
print(cube(3))

print("---------------")
print(power(2))
print(power(2,3))
print(power(x=3, num=2))

print("---------------")
print(multi_add(4,5,6,74,4))