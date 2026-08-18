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

