**Disclaimer:** This `.md` contains all the notes from the slides. For more in depth content, look through the exercises for Jupyter Notebook for each week. There <ins>will</ins> be things on the exam that are not covered here.

The <ins>exam</ins> will be on the following topics:
1. Syntax for different data types
2. Conditional statements and Loops
3. Indexes for list and string
4. Naming conventions (variables, functions and classes)
5. Basic programming keywords in python (for, while, class, def, ...)
6. Basic printing techniques (print without line break, print variables with messages)
7. Common built-in functions and how to use them (input(), len(), ...)
8. Files and exceptions handling
9. Basic concepts (attributes/methods) associated with class/objects and how to use them → first session from OOP

### misc notes:
`break` = stop the loop completely.  
`continue` = skip this round, but keep looping.

# Class Notes

## 14/04/26 Notes (week 1)

took no notes (intro to github and pycharm)

## 21/04/26 Notes (week 2)

A **high-level programming language** is close to human speech (eg. Python).  
A **low-level programming language** is closer to computer speech (eg. a = 010001).

### Programming Terminology

1. Statement
   - A statement performs actions (eg. `print("hello"), if x == 1`).  
2. Expression
   - Expression → Evaluation → Value (eg. `123, 1+2+3+4, n == 3`).  
4. Variables
   - A variable name should begin with a letter, and it can only contain letters, numbers and underscores.

Lowercase and uppercase letters are different characters. `word` , `Word` and `WORD` are three different variables.  
It is a common practice in Python to use only lowercase characters in variable names.  
For multiple words, use an underscore between the words (eg. `family_name`).  
     - A piece of memory that stores a value that can be changed (eg. `x = 1`).

`x = 1` is not the same as `x == 1`. `==` represents a conditional check "if x equals one".

### Different Variables

- string `"text"`
- int `394`
- float `3.1415926`
- boolean `True or False` *Must be uppercase, `false` would be wrong.
- list, tuple, range
- set, dict
- NoneType

A small block of code containing a conditional if-clause:
```
if semester == 2:
   print("Take Tech Basics I.")
elif semester == 3:
   print("Take Tech Basics II.")
else:
   print("No more Tech Basics!")
```
Keep in mind, the if, elif and else executes whatever is after the colon `:`.

### Python Operators
Operators are used to perform operations on variables and values.  
Includes arithmetic operators, assignment operators, comparison operators, logical operators, identity operators etc.

<ins>Arithmetic Operators</ins>  
| Operator | Name | Example |
| --| --| --|
| + | Addition | x + y |
| | Subtraction | x - y |
| * | Multiplication | x * y |
| / | Division | x / y |
| % | Modulus | x % y |
| ** | Exponential | x ** y |
| // | Floor Division | x // y |

<ins>Assignment Operators</ins>  
| Operator | Example | Same As |
| --- | --- | --- |
| = | x = 5 | x = 5 |
| += | x += 3 | x = x + 5 |
| -= | x -= 3 | x = x - 3 |
| /= | x /= 3 | x = x / 3 |

(there are more assignment operators, but none we have used in class.)

<ins>Comparison Operators</ins>  
| Operator | Name | Example |
| --- | --- | --- |
| == | Equal to | a == b |
| != | Not equal to | a != b |
| > | Greater than | a > b |
| >= | Greater than or equal to | a >= b |
| < | Less than | a < b |
| <= | Less than or equal to | a <= b |

<ins>Logical Operators</ins>  
Combine multiple conditions with: `and` , `or` and `not` (eg. `if a > b and a < c`).

<ins>Identity Operators</ins>  
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location (eg. `a is b`, `a is not b`).  
<sup>*Note it is **not** the same as `a == b`.</sup>

<ins>Truth Table</ins>  
| a | b | a and b | a or b |
| --- | --- | --- | --- |
| False | False | False | False |
| True | False | False | True |
| False | True | False | True | 
| True | True | True | True |

### Code Fixes

Consider the code:  
`result = 14 * 4`  
`print("The result is" + result)`

This results in an error.  
Corrections follow:  
1. `print(f"The result is {result}")`  
2. `print("The result is", result)`

A snippet of working code, determining prices for different ages:  
```
age = input("Enter your age:"))
age = int(age)
if age > 0 and age < 110:
    if age > 18:
        print("1 Adult Ticket")
    else:
        print("1 Discount Ticket")
else:
    print("Please enter a valid age!")
```

## 28/04/26 Notes (week 3)

trip to google

## 05/05/26 Notes (week 4)

### While Loop
- Executes a set of statements as long as **a condition** is true / is met.

`while <statement>:`  
`   <block>`  

An example:  
`n = 0`  
`while n < 5:`  
`   n += 1`  
`   print(n)`

### For Loop
- Interates over a sequence.

Can be either a list, a tuple, a dictionary, a set or a string.

`for <variable> in <collection>:`  
`   <block>`  

An example:  
`for x in range(6):`  
`   print(x)`

Using a `break` statement exits any code in a `for` or `while` loop.

### String Indexing

Assuming that `string = "Exemplary"`, the index is as follows:

<ins>Index</ins>  
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E | x | e | m | p | l | a | r | y |

These can be accessed wwith `string[2]` (which would return `e`).

You can also create Substrings, also known as Slicing.

`sub_string[begin : end]`  
`string = "Exemplary"`  
`sub_string = string[2:6]`
This would return `empl`, see Index above. Keep in mind the out-value isn't included (6, or `a`).

### Lists
- List is a sequence of heterogenous items
- New lists can be created with bracket notation

`my_list = []`  
`my_int_list = [1, 3, 5, 7, 9]`  
`my_fruit_list = ["apple", "banana", "mango"]`  

You can also index and slice lists.

Index: `first_item = my_int_list[0]`  (1)  
Slice: `sub_list = my_int_list = [:3]` (1, 3, 5)

<ins>List Methods</ins>  
| Method | Description |
| --- | --- |
| append() | Adds an element at the end of the list |
| clear() | Removes all of the elements from the list |
| copy() | Returns a copy of the list |
| count() | Returns the number of elements with the specified value |
| extend() | Adds the elements of a list (or any iterable), to the end of the current list |
| index() | Returns the index of the first element with the specified value |
| insert() | Adds an element at the specified position |
| pop() | Removes the element a the specified position |
| remove() | Removes the first item with the specified value |
| reverse() | Reverses the order of the list |
| sort() | Sorts the list |

##  12/05/26 Notes (week5)

### Functions
- A function is a block of code which only runs when called.

Python has some **built in** functions, like `len()`, `sorted()`, `print()`, `input()` etc.

A simple function:  
`def print_message():`  
   `print("This is my own function!")`  
`print_message()`

It is common practice in Python to name functions like variables (`open_folder` instead of `openFolder`).

Functions are:  
1. Reusable (no need to repeat code)  
2. Modularization  
3. Readability

Functions do not need an input or output.

### Arguments and Parameters

You can pass arguments into a function:  
`def message(text):`   # The text is called 'parameter'  
`   print("Message:",text)`  
`message("This si my own function!")`   # Argument  
`message("What does it do?")`

`def sum(x, y):`  
`   result = x + y`  
`   return result`  
`result = sum(1, 2)`  
`print(f"The sum is {result}")`

### Global Variables

- A global variable is a variable defined outside of any function.

`DEBUG = true`  
`def debug(message):`  
`   if DEBUG:`  
`      print(message)`  
`debug("This message will only be printed if DEBUG is true.")`

Why uppercase DEBUG?  
Values that won't be changed after initial definition are called **Constants**.  
These are commonly written in uppercase.  
`PI = 3.1415926`  
`URL = "https://api.example.com"` 
`API_TOKEN = 7034982315`

### Local Variables

`def my_function():`  
`   my_variable = 10`   # Variable is defined <ins>inside</ins> a function.  
`   print(my_variable)`

Global variables are fine for short, simple programs.  
You should try to avoid global variables with larger projects (global variables work across files, so if you have a global variable defined in **file_a** and you are in **file_b**, you cannot create two global variables with the same name, and they take up a lot of memory).

<ins>Comparison</ins>  
| Item | Global Variables | Local Variables |
| --- | --- | --- |
| Definition | Declared outside the functions | Declared within the functions |
| Scope | Can be accessed throughout the code | Can only be accessed inside the function |
| Value | Once the value changes it is reflected throughout the code | Once changed the variable doesn't affect other functions of the program |

### Functions inside a Function

```
def myfunc()
   x = 300
   def myinnerfunc():
      print(x)
   myinnerfunc()
myfunc()
```

### Main Function

A function for **greet.py**:

`def greet():`  
`   print("Hi!")`

`def special_print(text):`  
`   print("***", text, "***")`

`if __name__ == "__main__":`  
`   greet()`

Imported into **test.py** (text.py becomes the <ins>main</ins> function):

`import greet`  
`special_print("Hello")`

### Recursion

- Recursion is when a function calls itself.

```
def recursion(x):
   if x >= 0:
      return x;
   recursion (x-1)
print(recursion(10))
print(recursion(0))
print(recursion(-7))
```

print(recursion(5)) would print `5`, then stop.

### (some) Notes from jupyter exercise:

If there is no content inside a function yet, at least write pass to avoid error messages:  
`def my_function():`  
`   pass`

The following code gives an error:  
`def my_function():`  
`    my_variable = 10`   # A variable inside a function (local variable).  
`    print("my_variable", my_variable)`  
`print(my_variable)`   # Attempt to call a variable which it cannot find, since it isn't global.  

To print the following:  
`****`  
`****`  
`****`  
The code segment would look like this:  
```
def string_rect(string, w, h):
    for i in range(h):
        print(string * w)
string_rect('*', 4, 3)
```

You can use `*argument` for a flexible number of arguments (or `**argument` for a flexible number of keyword arguments):  
`def show_classes(*classes):`  
`    print("The first class is:", classes[0])`  
`show_classes("Technical Basics I", "Technical Basics II")`

This prints: `The first class is: Technical Basics I`.

## 19/05/26 Notes (week 6)

### Lists  
(covered a bit before)

- A collection of ordered, mutable, heterogenous elements.

`my_list = ["apple", "banana", "cherry"]`  
Arrays are for homogenous elements, with no built-in support in Python.

### Mutability

- An object is considered mutable if its value can be changed after it has been created.

Mutable Data types: `list`, `set`, `dictionary`.  
Immutable Data types: `int`, `float`, `bool`, `string`, `byte`, `tuple` (once a value has been set, its value cannot be changed).

### Reference

The value of a variable is actually not stored in the variable itself. What is stored in a variable is a **refrence**, information about the **location** in computer memory where the value can be found.  

`my_list = [1,2,3]`  
my_list   -->   [1] [2] [3] (in memory)

In the following code:
```
a = [1, 2, 3]
b = a
b[0] = 10
```
Then the memory for BOTH A and B becomes `[10] [2] [3]`.  
`a[0]` is also `10`.  
If we don't want this, and only want to copy the value, we use `copy` (`list2 = list1.copy()`).  

### Dictionary

- A collection of data stored as `key:value` pairs.  
- It's ordered, mutable, and does not allow duplicates in keys.

```
my_dict = {
   "name": "Lily Mustermann",
   "major": "Digital Media",
   "semester": 2,
   "exchange_student": False
}
```

<ins>Dictionary Methods</ins>  
| Method | Description |
| --- | --- |
| clear() |Removes all the elements from the dictionary |
| copy() | Returns a copy of the dictionary |
| fromkeys() | Returns a dictionary ith the specified keys and value |
| get() | Returns the value of the specified key |
| items() | Returns a list containing a tuple for each key-value pair |
| keys() | Returns a list containing the dictionary's keys |
| pop() | Removes the element with the specified key |
| popitem() | Removes the last inserted key-value pair |
| setdefault() | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| update() | Updates the dictionary with the specified key-value pairs |
| values() | Returns a list of all the values in the dictionary |

**Usage of Dictionaries:**
- Structured data: user profiles, mapping csv...  
- Lookup tables: ISO codes & values...  
- Storing settings  
- Counting frequency  
- Passing keyword arguments for functions

### Hash Table

- The inner working mechanism of dictionary, a layer of encryption (eg. SHA256).

An example: `a9s7h4fs768d7fa876d4gd978df`  
Very confusing.  

### Tuple

- A collection which is ordered, immutable (cannot be dynamically changed, e.g. adding numbers inbetween others), and allows duplicate values.

`point = (3,7)`  
Tuples are less used than other data types.

### Set

- A collection of different things.

`fruits = {"apple", "banana", "cherry", "tomato"}`  
`vegetables = {"potato", "cabbage", "tomato"}`

Sets are unordered, mutable and no duplicate variables.  
In a set, `True` and `1` are considered the same value. The same goes for `False` and `0`.  
You can add/remove items but not change them.  
SETS are not to be confused with `list()`.

<ins>Comparisons</ins>  
| List | Tuple | Set | Dictionary |
| --- | --- | --- | --- |
| list() | tuple() | set() | dict() |
| [1, 2, 3] | (1, 1) | {1, 2, 3} | {"name": "Eleri", "age": 22} |
| allows duplicates | allows duplicates | **does not allow duplicates** | allows duplicates in values but not in keys |
| mutable | **immutable** | mutable | mutable |
| ordered | ordered | unordered | ordered (Python 3.7 and above) |
| frequent modifications | immutability | uniqueness | key-value pairs |

### Solution to Task 3 from Jupyter Notebook

This is the code for the 3rd task:
```
import re

def word_counter(corpus:str):
    wordcount = {}   # (an empty dictionary)
       # Removes all special characters:
    corpus = re.sub('\\W+',' ', corpus)
       # Split the string into a list of words:
    words = corpus.split()
       # Look through the list:
    for word in words:
        word = word.lower()   # (make lowercase)
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    return wordcount

test_input = "This is a sentence that needs to be counted. Is the sentence long enough?"
print(word_counter(test_input))
```
Very confusing aaaaa

## 26/05/26 Notes (week 7)

### Categories of Errors

1. **Syntax Errors**: Missing colon `:`, missing quotation mark at the end of a string `print("Hello world)`.  
2. **Indentaiton Errors**: When the coe's spacing is not consistent.  
3. **Runtime Errors/Exceptions**: Only happen in specific marginal cases, and they halt the program after it runs.

Exceptions:  
It is possible to handle Exceptions so that the execution continues despite them occuring:
```
try:
   age = int(input("Please enter your age: "))
except:
   print("Something went wrong.")
else:
   print("Nothing went wrong.")
```

Typical Runtime Errors:  
1. `ValueError`: When the argument passed to a function is somehow invalid (`float("1,23")`).  
2. `TypeError`: When the value is of the wrong type (`len(10)`).  
3. `InexError`: When trying to refer to an index which doesn't exist (`list[5]`).  
4. `ZeroivisionError`: When trying to divide by zero (`sum(my_list / len(my_list)`).  
Of these, Value and Type errors are the most common.

Raising Exceptions:  
```
def age(x):
   if type(x) is not int:
      raise TypeError("Only integers are allowed.")
   if x < 0:   # Or a ValueError
      raise Exception("Sorry, the age needs to be greater than zero.")
   return x
```

## 02/06/26 Notes (week 8)

### Procedural Programming
A programming paradigm where a program is structured as a series of functions, that perform specific tasks.  
- Communication is done by passing arguments and returning values  
- It focuses on procedures and logic

### Object-Oriented Programming  
A programming paradigm that organizes software design around data, or objects, rather than functions and logic.  
- It binds certain data and functions in a structured way (similar to a dictionary)  
- Efficient, less code

### Classes
A class is the blueprint of an object:
```
class Item:

      # constructor
   def __init__(self, name, category,description):
         # attributes
      self.name = name
         # 'type' is not used because it is a reserved keyword in python
      self.category = category
      self.description = description
      self.used = False   # default values

      # method
   def use(self):
         # it does something deoending on the type
      self.used = True
```

Dictionaries, lists, and strings are pre-defined classes in Python.  
`my_list = [1,2,3]`  
`my_list.append()`  
When you create a list, you are creting an object/instance from the class `list`.

### Classes
- Shapes: rectangle, triangle, circle...

Classes are usually named in `camel case`. That means that all the words in the class name are written together without spaces, and each word is capitalized (`BankAccount`, `LibraryCard` etc.)

### Object
An object is an instance of a class.  
We can have many objects from the same class.  
Changing one object won't influence other objects of the same class.

```
torch = Item("torch","tool","Lights up dark places.")
key = Item("key","tool","Opens a locked door.")
torch.use()
```

<ins>Terminologies</ins>  
| Standalone | Associated with an object/class |
| --- | --- |
| Functions | Methods |
| Variables | Attributes |

### Special Methods/ Magic Methods
Python Magic methods are the methods starting and ending with double underscores `__`.  
They are also called **Dunder Methods**, which stands for "Double Under (Underscores)".
```
class SampleClass:
   def __init__():
      pass   # constructor method
   def __str__():
      pass   # override the default printing method
```

Optimized Jupyter Notebook Exercise:
```
class MensaCard:
    def __init__(self, name:str, balance:float):
        self.name = name
        self.balance = float(balance)

    def __str__(self):
        return f"{self.name}'s balance is {self.balance} euros."

    def eat_lunch(self, option:str):
        meal = 0
        if option == "A":
            meal = 2.3
        if option == "B":
            meal = 3.8
            
        if self.balance < meal:
            print("Low balance, please charge your card.")
            return False
        else:
            print(f"{self.name} eats lunch Option {option}. Balance is now {self.balance} euros.")
            
            return True

    def deposit_money(self, amount):
        if amount < 0:
            raise ValueError("Please don't deposit a negative number.")
        else:
            self.balance += amount
            print(f"{amount} euros has been added to {self.name}'s account. Balance is now {self.balance} euros.")

card1 = MensaCard("Lisa", 20)
card1.eat_lunch("B")
card1.eat_lunch("A")
print(card1)
```

My attempt at the same code (from Jupyter Notebook):
```
class MensaCard:
    def __init__(self, name:str, balance:float):
        self.name = name
        self.balance = float(balance)

    def __str__(self):
        return f"{self.name}'s balance is {self.balance} euros."
    def eat_lunch(self, choice:str):
        if choice == "A" or choice == "B":
            if choice == "A":
                if self.balance >= 2.3:
                    self.balance -= 2.3
                    print(f"{self.name} eats lunch Option A for 2.3 Euros.")
                    return True
                else:
                    print(f"{self.name} cannot afford meal Option A.")
                    return False
            elif choice == "B":
                if self.balance >= 3.8:
                    self.balance -= 3.8
                    print(f"{self.name} eats lunch Option B for 3.8 Euros.")
                    return True
                else:
                    print(f"{self.name} cannot afford meal Option B.")
                    return False
        else:
            return f"Invalid meal option (A or B)."

   def deposit_amount(self, amount:float):
    if amount > 0:
        self.balance += amount
        print(f"You added {amount} euros to {self.name}'s Card.")
    else:
        print("You must input an amount greater than 0.")

card = MensaCard("Jasper", 2)
card.eat_lunch("B")
deposit_amount(card, 10)
print(card)
```

## 09/06/26 Notes (week 9)
🚨 NOT REQUIRED FOR THE EXAM 🚨

### Mutability PART 2
Mutability allows you to create a list `[]` of objects and update each one individually.  

### Encapsulation
A common feature in object-oriented programming languges: Classes can usually hide some of their attributes from the outside.  
- If you don't want attibutes to be edited.

Hidden attributes are usually called `private`. In Python this is achieved by adding two underscores `__` to the beginning ofthe attribute name.

Example with Setters and Getters:
```
class Cola:
      # below the attribute ingredients is private, while the attribute name is accesible
   def __init__(self, ingredients: list, name: str):
      self.__ingredients == ingredients
      self.name = name

   def get_ingredients(self):   # getting a private attribute
      return self.__ingredients

   def set_ingredients(self, ingredients:list):
         # below we can add more constrains here to protect the ingredients attribute
      self.__ingredients = ingredients # setting a private attribute
```

### Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.  
- _Parent class_ is the class being inherited from, also called base class.  
- _Child class_ is the class that inherits from another class, also called derived class / sub class.

### Protected Attibutes
Protected Attributes are accessible to sub classes but not to outside. In Python this is achieved by adding one underscore `_` to the beginning ofthe attribute name.

<ins>Terminologies</ins>  
| Access Modifier | Example | Visible to Client | Visible to Derived Class |
| --- | --- | --- | --- |
| Public | self.name | yes | yes |
| Protected | self._name | no | yes |
| Private | self.__name | no | no |

End of `.md` notes. Thanks for reading :3

## 16/06/26 Notes (week 10)

### Streamlit
- Used to build data-based web applications (Data Science, LLMs, ...)
- Browser-based Interface
- Easy Development

held exam

## 23/06/26 Notes (week 11)

went over the exam answers
