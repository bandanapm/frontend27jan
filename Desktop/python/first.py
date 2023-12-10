# def main():
#     print("Hello world!!!")
#     name = input("What is your name?")
#     print(name)

# if __name__ == "__main__" :
#     main()

myList = [1,"Bandana", "M1P5C2",4,5,6,7]
myTuple = (1,"Bandana", "M1P5C2")
# if I want to print only third item from myList and myTuple then
print(myList[2])
print(myTuple[2])

# if I want to print from second item
print(myList[1:6])
# print(myList[kun bata print garenry: katti otta number samma ])

# if I want to print from some place up to some skipping some
print(myList[2:7:2])
# print(myList[un bata print garenry: katti otta number samma :aani kun choose garyeko xa 1st maa tesko bata kun position maa print gareny])

# to print in reverse
print(myList[::-1])

# to print disctionary it should have unique kye which is inside ""
mydist = {"my":1,"name":2,"is":3}
print(mydist["my"])

# global and local variable
myStr = "Global"
def someFunction():
    myStr = "Local"
    print(myStr)

someFunction()
print(myStr)

# above lines print the local variable but after take global var
# to take all local variable do this
myStr = "Global"
def someFunction():
    global myStr
    myStr = "Local"
    print(myStr)

someFunction()
print(myStr)

# to delete value
del myStr
print(myStr)


