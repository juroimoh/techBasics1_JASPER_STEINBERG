# Class Notes

## 14/04/26 Notes

took no notes (intro to github and pycharm)

## 21/04/26 Notes

A **high-level programming language** is close to human speech (eg. Python).  
A **low-level programming language** is closer to computer speech (eg. a = 010001).

### Programming Terminology

1. Statement
   - A statement performs actions (eg. `print("hello") , if x == 1`).
2. Expression
   - Expression → Evaluation → Value (eg. `123 , 1+2+3+4 , n == 3`).
4. Variables
A variable name should begin with a letter, and it can only contain letters, numbers and underscores.
Lowercase and uppercase letters are different characters. `word` , `Word` and `WORD` are three different variables.
It is a common practice in Python to use only lowercase characters in variable names. For multiple words, use an underscore between the words (eg. `family_name`).
     - A piece of memory that stores a value that can be changed (eg. `x = 1`).

`x = 1` is not the same as `x == 1`. == represents a conditional check "if x is equal to one".

### Different Variables

- string `"text"`
- int `394`
- float `3.1415926`
- boolean `True or False` *Must be Uppercase, `false` would be wrong.
- list, tuple, range
- set, dict
- NoneType

A small block of code containing a conditional if-clause:
```
if semester == 2:
   print("Take Tech Basics I)
elif semester == 3:
   print("Take Tech Basics II)
else:
   print("No more Tech Basics!")
```
Keep in mind, the if, elif and else executes whatever is after the colon `:`.

### Python Operators
Operators are used to perform operations on variables and values.
Includes arithmetic operators, assignment operators, comparison operators, logical operators, identity operators etc.

<ins>Arithmetic Operators</ins>  
| Operator | Name | Example |
| --- | --- | --- |
| + | Addition | x + y |
| - | Subtraction | x - y |
| * | Multiplication | x * y |
| / | Division | x / y |
| % | Modulus | x % y |
| ** | Exponential | x ** y |
| // | Floor Division | x // y |

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
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location (eg. `a is b , a is not b`).  
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

This results in an error. Corrections follow:  
`print(f"The result is {result}")`  
`print("The result is", result)`

A snippet of working code, determining prices for different ages:  
`age = input("Enter your age:"))`  
`age = int(age)`  
`if age > 0 and age < 110:`  
`    if age > 18:`  
`        print("1 Adult Ticket")`  
`    else:`  
`        print("1 Discount Ticket")`  
`else:`  
`    print("Please enter a valid age!")`

## 28/04/26 Notes

trip to google

## 05/05/26 Notes

took no notes (introduction to indexing, while and for loops, and turtle)

## 12/05/26 Notes

### Functions

- A function is a block of code which only runs when called.

Built into python:
`print(), len(), input()`  

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

### Functions inside a Function

`def myfunc()`  
`   x = 300`  
`   def myinnerfunc():`  
`      print(x)`  
`   myinnerfunc()`  
`myfunc()`

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

`def recursion(x):`  
`   if x >= 0:`  
`      return x;`  
`   recursion (x-1)`  
`print(recursion(10))`  
`print(recursion(0))`  
`print(recursion(-7))`

print(recursion(5)) would print `5`, then stop.

### Notes from exercise:

If there is no content inside a function yet, at least write pass to avoid error messages:
`def my_function():`  
`   pass`

The following code gives an error:
`def my_function():  `
`    my_variable = 10  `   # A variable inside a function (local variable.  
`    print("my_variable", my_variable)  `
`print(my_variable)` # Attempt to call a variable which it cannot find, since it isn't global.

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

