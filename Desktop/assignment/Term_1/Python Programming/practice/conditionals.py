
"""
Conditionals/if else statements
"""


print(f"type of True and False: {type(True)}")

"""
Default values of integer, lists and dictionaries are True or False depending on the data.
An empty list/dict has a bool value of False. Non empty list has bool value of True
"""
print(f"0: {bool(0)}, 1: {bool(1)}")
print(f"empty list: {bool([])}, list with values: {bool(['woop'])}")
print(f"empty dict: {bool({})}, dict with values: {bool({'Python': 'cool'})}")

"""
Conditional expressions
"""
print(f"{1 == 0}")
print(f"{1 != 0}")
print(f"{1 > 0}")
print(f"{1 > 1}")
print(f"{1 < 0}")
print(f"{1 < 1}")
print(f"{1 >= 0}")
print(f"{1 >= 1}")
print(f"{1 <= 0}")
print(f"{1 <= 1}")
# you can combine these
print(f"{1 <= 2 <= 3}")

"""
and/or/not conditions
"""
python_is_cool = True
java_is_cool = False
empty_list = []
secret_value = 3.14
print(f"Python and java are both cool: {python_is_cool and java_is_cool}")
print(f"secret_value and python_is_cool: {secret_value and python_is_cool}")
print(f"Python or java is cool: {python_is_cool or java_is_cool}")
print(f"{1 >= 1.1 or 2 < 1.4}")
print(f"Java is not cool: {not java_is_cool}")

"""
You can combine multiple statements, execution order is from left to right. You can control the execution order by using brackets.
"""
print(bool(not java_is_cool or secret_value and python_is_cool or empty_list)) # True
print(bool(not (java_is_cool or secret_value and python_is_cool or empty_list))) # False

"""
If statements
"""
statement = True
if statement:
    print("statement is True")

if not statement:
    print("statement is not True")

empty_list = []
# With if and elif, conversion to `bool` is implicit
if empty_list:
    print("empty list will not evaluate to True")  # this won't be executed

val = 3
if 0 <= val < 1 or val == 3:
    print("Value is positive and less than one or value is three")

my_dict = {}
if my_dict:
    print("there is something in my dict")
else:
    print("my dict is empty :(")


"""
if elif else
"""
val = 88
if val >= 100:
    print("value is equal or greater than 100")
elif val > 10:
    print("value is greater than 10 but less than 100")
else:
    print("value is equal or less than 10")

# You can have as many elif statements as you need. In addition, else at the end is not mandatory.
greeting = "Hello fellow Pythonista!"
language = "Italian"

if language == "Swedish":
    greeting = "Hejsan!"
elif language == "Finnish":
    greeting = "Latua perkele!"
elif language == "Spanish":
    greeting = "Hola!"
elif language == "German":
    greeting = "Guten Tag!"

print(greeting)