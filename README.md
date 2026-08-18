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

