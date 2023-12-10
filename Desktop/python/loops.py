def main():
    x = 0

    # while loop
    while(x < 5):
        print(x)
        x = x + 1

    # for loop
    for x in range(5,10):
        print(x)

    # use for loop over a collection
    day =["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for d in day:
        print(d)

    # use the break and continue statement
    for x in range(5,10):
        if x == 7:
            break
        if x % 2 == 0:
            continue
        print(x)


    # using the enumerate() function to get index
    day =["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i,d in enumerate(day):
        print(i,d)

main()