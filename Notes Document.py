import math
#Notes Document

#Comments
'''A comment is used to show what is happening on each line.
It can be used to help debug and to help others know what is happening. '''

#A hash can be used for single line comments such as this one
'''3 speech marks can be used to create a block code.'''

#Data types

Integer = int(1)    #An integer is a whole number
String = str("Hello World")     #A string is a line of text or characters
Float = float(5.3)      #A float is a decimal number it is also known as a real number
Char = ("F")       #A single character
Boolean = ("true")       #True or false

#structured and elementary data types

'''You can cast a variable by either implicit or explicit casting
Implicit casting is letting the program guess what the data type is
Explisit casting is specifically telling the program what type it is.'''

#Common arithmatic operations
num1 = 10
num2 = 11
add = (num1 + num2)
multiply = (num1 * num2)
subtract = (num1 / num2)
minus = (num1 - num2)
square = (num1 ** num2)

'''To round a number you must use the round function in a variable and then print it'''
x = round(3.5)

'''To truncate a number (Remove decimal) you must first import math then use the math.trunc() function'''
truncate = int(123.26)
truncate = math.trunc(truncate)
print(truncate)

'''Div returns the divided number '''
div1 = 2 // 3
print(div1)
'''Mod returns the remainder'''
mod1 = 3 % 2
print(mod1)

#String handeling
testString= str("This is a test").title    #Makes the first letter a capital
testString = str("This is a test").upper    #Makes the string upper case
testString = str("This is a test").find("is")     #Looks for a string within a string

'''Gives you the ascii value of a character'''
Ord = ord("t")
print(Ord)

#Concatenation
'''Basically just sticking 2 strings together. '''
String1 = ("My name is ")
String2 = ("Will")
String3 = (String1 + String2)
print(String3)

#Variables and Constants
'''A variable is a value that can be changed. A constant is a value that is set and cannot be changed'''
variable = int(input("How old are you? ")) #This allows the user to input any number as their age.
Constant = int(13)      #This is a set constant that cannot be changed without editing the code.

#Relational operators
'''A relational operator is something such as: '''

'''
EqualTo == "3"
DoesNotEqual != "3"
MoreThan = 3 < 1
LessThan = 3 > 4
'''

#Selection
'''Selection is things like If statements'''
'''Example: '''
ifstatement = 1
if ifstatement == 1:
    print("This is equal to 1")
elif ifstatement != 1:
    print("This is not equal to 1")     #This is a way of addind more conditions to the if statement such as more than 3 or less than 10

else:
    print("This is not a number")   #This is a catch all. This means that any other statement is selected eg a string when a number is wanted.

#Nesting is where an if statement it put inside an if statement. It is done by indenting everything.

score = 154
money = 154

if money == score:
    print("Money = score")
    if score > money:
        print("More score")
        if score < money:
            print("More money")


#And
#or         Selects a b and both
#not
#exor       Selects only A and B


#Case statements
'''A case staement is similar to an if statement however when there are more than 5 conditions'''

#Itteration
''' itteration is any kind of loop. In puthon this can be a while loop or any other type.'''
#Example:
whileloop = 4
while whileloop == 4:
    print ("Duck")
    break

'''Repeat until loop is the same as a while loop however the check is at the end of the loop.
This means that it will loop over and over until the output is correct.'''

shift = str(input("Input a word"))
for character in shift:
    character = ord(character) + 1
    #print(character)
    x = chr(character)
    print (x)


#Arrays
'''Arrays are a way of storing multiple different data types. '''
'''An array is written in square brackets with each value seperated by commas.
Each value is represented in index (Starting from 0 as the first one and counting up).
A multidimentional array is an array that contains many more smaller arrays.'''
array = ["James", "Ben", "Ellie", "Kitty", "Lily"]   #This is a normal array. It contains a collection of values (in this case my friend's names)
MultiArray = [["James", "16",], ["Ben", "16"], ["Kitty", "17"]]   #This is a multidimentional array, It contains smaller arrays of names and ages.

'''There are a fre commands where you can append (add) and pop (remove and return) items from the array.
eg. Append, Pop, insert, count'''

ForloopArray = []
for number in range(1,11):
    ForloopArray.append(0)
for i in range (1,11):
    print(ForloopArray)

array = [[0 for i in range(10)] for i in range (1)]
for i in array:
    line = " "
    for x in i:
        line = line + str(x) + " "
print(line)


#Subroutines
'''a subroutine is a section of code that cen be reused by stating its name. It is an umbrella term for functions and 
procedures.
A Function returns a value and a Procedure doesn't, however a procedure can store the value.
For example: Print is a procedure
             Len is a function because it returns the length.'''


#Language defined functions and prodecures are already built into languages

#Modular programming is the process of breaking down programs into a number of subroutines.

#Files and exeption handeling.
'''If you want to store data and save it for later you can save it in a text file. Sometimes you can save it in a database but
generally it is easier to save it in a text file. Each row in a text file may contain may fields of 1 peice of data.'''

#ADD READING AND WRITING TO TEXT FILES HERE


#Exeption handeling
'''This is a way of preventing errors in your code. You tell the code to TRY something and EXEPT the errors. This prevents your code from crashing
 because when an error happens, it prints an error message rather than crashing the program.'''

#Dictionary
''' Written in curley brackets and sperated by commas e.g.'''
dictionary = {"1", "2", "3", "4"}
'''These are typically un-ordered and can be is any order.'''