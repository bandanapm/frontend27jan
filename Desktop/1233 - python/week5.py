"""
# menu driven programming
# files
# What is files?-> File is the most primitive way of storing information on secondary storage.
# There are two types general types of files that you can utilize in any progeamming
# language?
# 1) Text files 2) DATA files (Binaries)
#  Text file: all the inputs and outputs are in the form of string

************* Procedure of using a file *****************
1) open/create a file you create a file object which contain the location
2) set the mode : (w)rite or (R)ead
 recurser or trunketor is set at the 1st line blinking

a="AFDBRTGBA"
print(a.rstrip('A'))
this will remove A from the right side
print(a.lstrip('A'))
this will remove A from the left side
print(a.strip('A'))
this will remove A from the both side



Create menu where the user can be sales record

"""
import os.path


def menu():
    print('------------------------Sales Record-----------------')
    print('1- record a new sales')
    print('2- adding sales to existing file')
    print('3- display file info')
    print('4- exit')
    return input('Enter 1,2,3 and 4')

def newSales():
    fileName = input('enter the file name: ') + '.txt'
    if not os.path.exists(fileName):
        with open(fileName,'wt') as afile:
            while True:
            n_sales = input(f'enter number of sales you like to record {fileName}')
            if n_sales.isdigit():break
            else:print('input must be an integer')
    else:
        print(fileName, 'is exist! you can add to menu 2 sales')
def addSales():pass
def displayFiles():pass

def salesProgram():
    choice = menu()
    if choice=='1':newSales
