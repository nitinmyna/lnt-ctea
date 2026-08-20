
DAY3 20-08-2026

Type Casting DONE
Lambda functions  
IDE and Python Shell DONE

employees = [
{"name": "Ravi", "salary": 50000},
{"name": "Anil", "salary": 80000},
{"name": "John", "salary": 60000}
]

## employees.sort(key=lambda emp: emp["salary"])

orders = [5000, 12000, 8000, 25000, 15000]
high_value = list(filter(lambda amount: amount > 10000, orders))
print(high_value)

It allows you to pass behavior as a value.
sorted(employees, key=lambda e: e["salary"])
lambda e: e["salary"]
"For each employee, use the salary as the value by which you should sort."

Type Casting:
Conversion of one type data into another.

int number = 0;
float number = 0.0; // Type casting happens. Error in case of Java
String name = null;

float number = 0.0; // Type casting happens. Error in case of Java
0.0 is a double type of value.
double is 8 bytes and float is 4 bytes.
We are trying to store 8 bytes of value into a 4 bytes of variable. DOWN CAST.
In the case of down cast there is chance of the data getting either lost or modified.

int number = 5.5;
5.5 from double to 5 which is int. So the precission part is lost.

float number = 538878945.0099670;
Here the float variable cannot store such a big number. We need double type of variable to store this big number. Modulo operation w.r.t. the size of the variable is done and the resutant value is stored.

byte number = 150; // out of range
In one byte we can store a value in range -128 to +127
1000 0000 (Here the MSB bit (left most bit) is one, means the number is -ve)
-1 * 2(7) = -128
0111 1111 = 1*2(6) + 1*2(5) + ..... 1*2(0) = 127

We tried to store 150 in 'number' but -105 is stored.

Up-Cast:
double number = 5.5f;
In up-cast there is no loss/change of data but there is certaining loss of memory.

Types-Casting must be avoided. Because they like adjustments.

Types casting in Object Oriented.

Zomato
admin zomato management
customer restaurants
endCustomer people who order food via Zomato

admin
id
name
phoneNumber
password

    addCustomr()
    deleteCustomer()
    updateCustomer()

endCustomer
id
name
type
age
gender
location
phoneNumber
address
cardDetails

    searchFood()
    searchRestaurant()
    setLocation()
    addItemToCart()
    placeOrder()
    cancelOrder()

class Customer
id
name
restaurantName
type

    CreateCustomer()            creating object
    InitializeCustomer()        constructors
    readCustomerDetails()       getter methdos Accessors
    setCustomrDetails()         setter methods Mutators
    compareCustomer()           equals()   ==   or  is operators
    printCustomer()             toString()  __str__()

POJO Plain Old Java Object
POPO

CRUD Operations (add one object/record, search one, update one, search one, list all)
class CustomerOperations

class Customer

class PriotrityCustomer extends Customer
Certain new features are given/added
Few of the features are refined (overridden)

Customer customer = new Customer();
PriotrityCustomer priorityCustomer = new PriotrityCustomer();

Customer customer = new PriorityCustomer();
Parent type reference references child type object.
However, using the reference here, we cannot access the newly added features of PriorityCustomer.

customer = priorityCustomer; //
priorityCustomer = customer; //

---

Say we are developing a project.
Once completed, we have the code.
The IDE must help us in development
Coding
Organising the files and folders (Explorer)
Helps in auto connecting to some of the VCS (github)
Debugging (using break point, watch point etc)
We can add 3rd partyu Apps to our IDE (Extensions)
Cyclomatic Complexity (To check number of paths in a logic/function)
Build and Release management

map To map/access each element in the list/array
filter To filter the i/p list on some condition
reduce reduce is to deduce/calculate some value (Sum or Avg etc.)

high_value = list(filter(lambda (amount, location): amount > 10000 and location == 'mumbai', orders))

We can use lambda to implement group-by
We can use lambda to implement group-by and having clause.

```
lambda for LISP programming
Autocad, to draft based on DCL files and I/Ps
```

Pandas Syntax:
allowed_regions = ["North", "South", "East"]
filtered_regions = df[df["Region"].isin(allowed_regions)]

SQL Syntax:
select \* from employees wher region in["North", "South", "East"];
// Returns the result set

filtered_regions = df[df["Region"].isin(["North", "South", "East"])]
// returns the data frame

sales_by_region = df.groupby("Region")["Sales"].sum().reset_index()

## select sum(amount) as Total_Sales from sales group by (region);

## DATA VISUALIZATION

Result Analysis
Assume that a college wants to do analysis on their semester exams.
Top 3 students for each subject Compare them with previous year data
Average score of each subject Year wise improvement w.r.t subject
Average score of each dept Dept wise performance
First 3 students scoring least marks Students who need more attention
Highest scored subject Which subject has done well
Least scored subject Which subject need more time

Sales Data
Expenses Data
Inventory Data
Raw Material Purchase data

OLAP Analysis huge amount of data is generated Less data manipulation
OLTP Transactions less amount of data is generated More data manipulation

OLAP is where we do data Analysis.

Line Chart is used to compare the on going score of chasing team vs the score of opponent team in Cricket.

I/P is PDF files
Processing data from PDF and creating the O/P back in form of PDF

---
