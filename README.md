# lnt-ctea

Repo is created to share the documents of the 3 days of Python training for LnT CTEA

---

## APPLICATIONS & LIBRARIES TO BE INSTALLED

VS code (IDE to run programs and development, To make notes)
Python (python.prg\downloads)
Libraries/Modules: pandas, numpy, matplotlib, seaborn
git (if github can be used or required)

Link to download VS Code: (Community Edition)
https://code.visualstudio.com/download?_exp_download=fb315fc982
Note: Click on the Blue button with the text (Windows 10, 11)
This downloads the installer/setup (.msi) file
Alomost all systems today are of 64 bit (So select x64)
Alternatively we can download the zip file and just extract the zip file and you can find the short cut for the VS code in the extracted folder.
Later we must double click the installer file and install the App.
This creates a CLI/Command "code" using which we can run the VS Code App

Link to download Python:
https://www.python.org/downloads/
Note: For windows machines, just use the Yellow Button

---

### Python Notes:

Python is a Dynamically typed Language.

```
float inputNumber = 0.0f;
employeeAge = 30
```

static memory allocation
dynamic memory allocation

Flight flight; // w.r.t. C++ flight here is an object which will be created in the Stack area.

Flight\* flight = new Flight(); // C++ syntax to create object in the Heap
Flight floght = new Flight(); // Java Syntax
Flight flight; // In Java flight here is just a reference created inside the frame of the function(Stack Area). It is not an object.

---

## Using the Libraries/Modules

```
import sys
sys.argv

import rootPackage.subPackage.subPackage;
```

Template: object.property
The dot operator has Left to Right associtivity

In Python strictly there is no primitive type. Everything is an object including the functions/methods.
That is to say everything has some information which we can make use of.

```
x, y, z = 10, 20, 30
```

First the values on RHS which are 10, 20 and 30 (in that order, L to R) are taken and stored into a immutable/un-modifyable list (tuple).

```
coordinates = (45.5152, -122.6784)
latitude, longitude = coordinates
```

---

## SET

A set is a data structure with unique elements.
We are not concerened with what is stored 1st or last.
Hence we may not use the subscript.

## TYPE CASTING

In Python there is no Implicit Type-Casting.

### In Java,

```
System.out.println("Age of the Giza Pyramids is at least" + 4500 + " years");
```

This is fine in Java (It implicitly invokes toString() method)

### In Python,

```
print("Age of the Giza Pyramids is at least" + 4500 + " years") # ERROR
```

You cannot concatinate a string with an int data.
You have to explicitly type cast the int value 4500 into a str value.

---

In Python, there is no implicit Type-Casting (Automatic Type casting). Rather, only explicit casting is allowed.

Because Type-Casting are Hinderence. It is usually a Design-Error.
So we must avoid them.

The Down cast is dangerous because the value it self may chage.
The up-cast is not dangerous but consumes more memory.

---

## Clean Coding (Good Coding Practices / Industry Standards)

1. Avoid using global variables (It creates Tightly Coulped solutions)
2. Consume the boolean values. Do not check them explicitly:
   sorted = True
   if sorted == True: # This is Bad
   pass
   if sorted: $ Thi is ggod.
   pass

3. When ever we are compring a variable with a literal, put the literal on RHS
   if number == 80 # Good
   if 80 == number # Bad
4. Names must be descritpve and self explanatory (unambigious)
   num, age, roi # Bad Names
   number (input_number), employeeAge, rate_of_interest # Good
<!--  -->
```
import sys

print(sys.argv)
print(type(sys.argv))
print(sys.argv[0])
print(type(sys.argv[0]))
```

---

## FUNCTION OVERLOADING WHICH IS NOT AVAILABLE IN PYTHON

dictionary = dict() # created a dictionary object

dictionary.get('mysuru') # get me the value where in the key is 'mysuru'
dictionary.get('mysuru', 100) # get me the value where in the key is 'mysuru', if not present me, use/return the value 100

As we know, in Java, the indexOf() method of String class is defined 4 times. Thus there are 4 different function definitions/implementation.

range() of Python:
range(10)
Start from 0 and go upto 9 with an default increment of 1 [0, 10)
range(5, 15)
Start from 5 and go upto 14 with an default increment of 1 [5, 15)
range(30, 50, 3)
Start from 30 and go upto 49 with an user given increment of 3 [30, 50)
range(100, 50, -2))
Start from 100 and go upto 51 with an user given increment of -2 [51, 100)

However, there is only one definition of range() with all 4 logic implemented conditionally (depending on the number of arguiments and wherther the 3rd argument if present is +ve or -ve)

## Why there is no Function Overloading in Python?

As we know the Python is Dynamically typed language and Python has features availble for functions/definitions such as: 1. variable number of arguments concept 2. Named arguments 3. default arguments

## What happens if we define 2 ore more functions with same name?

In such a case, only the last defined function/method will be stored/recorded in memory.

---

## Tuple

numbers = (10, 20) # numbers here is a tuple
numbers = (10, ) # numbers here is a tuple
numbers = (10) # Here numbers is just an int value
numbers = [19, 33] # numbers now is a list

---

DAY2 19-08-2026

## SLICING:

Applies for list and strings.

numbers = [23, 31, 11 , 13, 3, 5, 17, 19, 7]

numbers[::]
numbers[:]
numbers[:50] # No error though we are going beyond the boundary of the list
numbers[50] # IndexError
numbers[::-1] # This gives us exactly the reversed list of the input list
Slicing is immutable activity. It doesnt perform in-place.
numbers[-1:-50:-1] # Sllicing from the end 49 places in reverse

Division Operator: /
If both N and D (N/D) are integers, then integer division happens. That is it returns always an integer value.

10)45(4
40
5
Do not continue the division by taking the decimal point

In Python if we use / slash it means we wish to do floating point division.
10)45(4.5
40
50
50
00

If we want Integer division in Python, we should use //

45 // 10 is 4
45 / 10 is 4.5
45 // 10.0 is 4.0
45 / 10.0 is 4.5

Logical Operators in C/C++/Java/C# are:
& && | || !

But logical operators in Python:
and or not

if condition1 & condition2
DO THIS

if condition1 && condition2
DO THIS

In both of the above cases, the o/p doesnt change. But In the 1st case, the condition2 is also checked. Where as in the 2nd case, the 2nd condition is omiited when the 1st condition fails.

if x++ < y and a >= --b
DO THIS

++x
x++

sum = x++
sum = ++x

So in Python, the updation operators ++ and -- are also terminated.

Math Module
Math.sqrt() used to find the square root.

\*\* Power operator as well

result = number \*\* 0.5

However, we must note that in the expression:
2 ** 3 ** 2
The answer is 512 and not 64. This is because the \*\* operator has Right to Left associtivity.

for loop()
We use the for loop when ever we know the number of iterations before hand. That is before start of the loop and not before start of the Application.
When ever we decide to do something for a fixed number of times, we count.

while()
We use the loop when the number of iteartions are unknown.

for i in range(10):
pass

range(10)
Starts from 0 to goes upto 9
range(5, 20)
range(5, 20, 2)
range(50, 20, -3)
Strats from 50 and goes upto 20 with a decrement of 3

while True:
pass

print(f'i = {i}', end=' ') # Syntax of Python
console.log(`i = ${i}`) // Syntax of JS

i = 1
while(i <= 10)
if i % 5 == 0:
break
print(i)
i += 1
else:
pass

When ever the 'break' statement executes, the else part is skipped otherwise not.

def my_function():
for i in range(15):
print(i)
i += 3
print(i)

## Here, whyen the range() is called, the duty of range is to keep YIELDING the value to 'i' for every iteration. Thus range() doesn't return a value. Rather it YIELDS a value every time some is asking for it.

In newer versions of Python, we can add the argument datatyes and also the returntype of the function/method.
Example:

```
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!\n")
    file.write("This is a second line of text.")
```

```
import csv

data = [
    ["Name", "Age", "Profession"],
    ["Alice", 30, "Engineer"],
    ["Bob", 25, "Designer"],
    ["Charlie", 35, "Manager"],
]

with open("people.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

---

```
file = open("people.csv", "w")
writer = csv.writer(file)
writer.writerows(data)
file.close()
```
