# VoiceCoding
VoiceCoding is a program that will allow people to code in Python using their voice. Using different voice commands that can be found in the [documentation](#documentation), users can perform simple tasks in Python in an environment like the Python command-line interpreter.

## Documentation
### Commands

- Assign
 - structure: "assign" {say a [data type](#data-types)} {say a value} "to variable" {say the name of variable} 
 - assigns a value to a variable 
 - example inputs: "assign 10 to variable x", "assign list hello cut world to variable y"
 - example outputs: `x = 10`, `y = ["hello", "world"]`
- Print
 - structure: "print" {say a [data type](#data-types)} {say a value}
 - prints out a value 
 - example inputs: "print 10", "print hello comma world exclamation point"
 - example outputs: `print(10)`, `print("hello, world!")`
- Call
 - structure: "call" {say a function or [method](#methods-and-other-things) expression}
 - calls any function or method that may modify another piece of data
 - example inputs: "call variable x method append parameters 1", "call variable x method pop"
 - example outputs: `x.append(1)`, `x.pop()`

### Data Types

- Integer\* 
 - any whole number
 - structure: "integer"(optional) {say any whole number}
 - example inputs: "integer one", "twelve", "one hundred forty two"
 - example outputs: `1`,`12`, `142`
- String\* 
 - any piece of text
 - structure: "string"(optional) {say anything}
 - example inputs: "string hello comma world exclamation point", "space", "if you're reading this it's too late"
 - example outputs: `"hello, world!"`, `" "`, `"if you're reading this it's too late"`
- Float\*
 - a decimal number
 - structure: "float"(optional) {say any decimal}
 - example inputs: "float one point two", "three point one four one five nine"
 - example outputs: `1.2`, `3.14159`
- Boolean\* 
 - stores data as true or false
 - structure: "boolean"(optional) {either "true" or "false"}
 - example inputs: "boolean true", "false"
 - example outputs: `True`, `False`
- Variable 
 - stores data types
 - structure: "variable" {any name}
 - example inputs: "variable x", "variable hello world"
 - example outputs: `x`, `hello_world`
- Equation
 - for math and simple string concatenation
 - structure: "equation" {say a [data type](#data-types)} {say a value} {say an [operator](#methods-and-other-things) {say a [data type](#data-types)} {say a value} ... 
- List 
 - ordered group of different Python objects
 - structure: "list" {say a [data type](#data-types)} {say a value} "cut" {say a [data type](#data-types)} {say a value} ...
 - example inputs: "list", "list one cut two cut three", "list hello cut one point five"
 - example outputs: `[]`, `[1, 2, 3]`, `["hello", 1.5]`
- Tuple 
 - immutable sequence of Python objects 
 - structure: "tuple" {say a [data type](#data-types)} {say a value} "cut" {say a [data type](#data-types)} {say a value} ...
 - example inputs: "tuple", "tuple one cut two cut three", "tuple hello"
 - example outputs: `()`, `(1, 2, 3)`, `("hello",)`
- Set 
 - group of unordered, unique Python objects 
 - structure: "set" {say a [data type](#data-types)} {say a value} "cut" {say a [data type](#data-types)} {say a value} ...
 - example inputs: "set", "set one cut one cut three", "set hello cut one point five"
 - example outputs: `set()`, `{1, 3}`, `{"hello", 1.5}`
- Function
 - blocks of code that can perform action on parameters
 - structure: "function" {say a function name} "parameters" {say a [data type](#data-types)} {say a value} cut ...
 - example inputs: "function list parameters hello", "function int params string ten"
 - example outputs: `list("hello")`, `int("10")`

<sup>*Doesn't have be explicity defined when using this data type in a command; ie: you can just say "one" instead of "integer one" to get the result of `1`.</sup>

### Methods and Other Things

- Methods
 - blocks of code that are called on class instances to perform actions
 - structure: {say a [data type](#data-types)} {say a value} "method" {say a method name} "parameters" {say a [data type](#data-types)} {say a value} cut ...
 - example inputs: "variable x method append parameters one", "space method join params function list params hello"
 - example outputs: `x.append(1)`, `" ".join(list("hello"))`
- Operators
 - for use in equations
 - `+` - "plus"
 - `-` - "minus"
 - `*` - "times", "multiplied by"
 - `/` - "divided by"
 - `**` - "to the power of"
