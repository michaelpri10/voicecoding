# VoiceCoding
VoiceCoding is a program that will allow people to code in Python using their voice. Using different voice commands that can be found in the [documentation](#documentation), users can perform simple tasks in Python in an environment like the Python command-line interpreter.

## Documentation
### Commands

- "assign" [[data type](#data-types) {value}] to ["variable" {name}] - assigns a value to a variable - ie: `x = 10`, `y = "hello, world!"`, `z = y`
- "print" [[data type](#data-types) {value}] - prints a value - ie: `print(10)`, `print("Hello, world!")`, `print(x)`

### Data Types

- integer\* - any whole number - ie: `1`, `10`, `1587`, `234891`, `-4`, `-25`
 - command: "integer one" or just "one"
- string\* - any piece of text - ie: `"hello, world!"`, `"my name is Michael"`, `"coding by voice"`
 - command: "string hello world" or just "hello world"
- boolean\* - stores data as true or false - ie: `True`, `False`
 - command: "boolean true" or just "true"
- variable - stores data types  - ie: `x`, `banana`, `hello_world`
 - command: "variable x"
- list - groups other data types together - ie: `[1, 2, 3]`, `["hello", "world"]`, `[x, y, z]`
 - command: "list" [[data type](#data-types) {value} cut [data type](#data-types) cut ...]
- equation - for math and simple string concatenation - `1 + 1`, `4 * 6`, `3/7`, `"hello" + "world"`, `"hello world" * 5`
 - command: "equation" [[data type](#data-types) {value} math operand [data type](#data-types) {value} math operand ...]

\*<sup>Doesn't have be explicity defined when using this data type in a command. You can just say "one" instead of "integer one" to get the result of `1`.</sup>
