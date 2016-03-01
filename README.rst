voicecoding
===========

.. image:: https://img.shields.io/pypi/v/voicecoding.svg
    :target: https://pypi.python.org/pypi/voicecoding/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/voicecoding.svg
    :target: https://pypi.python.org/pypi/voicecoding/
    :alt: Downloads

.. image:: https://img.shields.io/pypi/pyversions/voicecoding.svg
    :target: https://pypi.python.org/pypi/voicecoding/
    :alt: Supported Python Versions

.. image:: https://travis-ci.org/michaelpri10/voicecoding.svg?branch=master
    :target: https://travis-ci.org/michaelpri10/voicecoding
    :alt: Status

About
-----

voicecoding is a program that will allow people to code in Python using their voice. Using different voice commands that can be found in the `documentation <#documentation>`__, users can perform simple tasks in Python in an environment similar to the Python command-line interpreter. voicecoding is currently only a command-line application, but the plan is for it to eventually become a full Python IDE controlled completely by voice, while still staying open source and free. You can check this project out on `PyPi  <https://pypi.python.org/pypi/voicecoding>`__ or fork it on `Github <https://github.com/michaelpri10/voicecoding>`__.

After you've `installed <#installation>`__ the program, you can run it by typing

``python -m voicecoding``

in your command prompt or terminal.

Installation
------------

On all operating systems, you first need to install the program itself using ``pip``:

``pip install voicecoding``

That will also install `SpeechRecognition <https://pypi.python.org/pypi/SpeechRecognition/>`__ which voicecoding depends on. You will have to manually install `PyAudio <https://people.csail.mit.edu/hubert/pyaudio/>`__, the other library that voicecoding depends on. The method of installation varies by operating system.

Microsoft Windows
~~~~~~~~~~~~~~~~~

You can simply just use ``pip``:

``pip install pyaudio``

Mac OS X
~~~~~~~~

First, you must install the PortAudio library with ``brew`` and then use ``pip`` to install PyAudio:

``brew install portaudio``

``pip install pyaudio``

Ubuntu/Debian
~~~~~~~~~~~~~

Run:

``sudo apt-get install python-pyaudio python3-pyaudio``

If that does not work, you should just try installing with ``pip``:

``pip install pyaudio``

Documentation
-------------

Commands
~~~~~~~~

Assign
''''''

-  structure: "assign" {say a `data type <#data-types>`__ and a value}
   "to variable" {say a name for the variable}
-  assigns a value to a variable
-  example inputs: "assign 10 to variable x", "assign list hello cut
   world to variable y"
-  example outputs: ``x = 10``, ``y = ["hello", "world"]``

Print
'''''

-  structure: "print" {say a `data type <#data-types>`__ and a value}
-  prints out a value
-  example inputs: "print 10", "print hello comma world exclamation
   point"
-  example outputs: ``print(10)``, ``print("hello, world!")``

Call
''''

-  structure: "call" {say a function or `method <#methods>`__
   expression}
-  calls any function or method that may modify another piece of data
-  example inputs: "call variable x method append parameters 1", "call
   variable x method pop"
-  example outputs: ``x.append(1)``, ``x.pop()``

Import
''''''

-  structure: "import" {say any module name}
-  imports a module to allow its method to be used
-  example inputs: "import math", "import web browser"
-  example outputs: ``import math``, ``import webbrowser``

If/Elif/Else
''''''''''''

-  structure: "if comparison"(comparison is optional) {say a
   `comparison <#comparison>`__} "elif comparison"(comparison is
   optional) {say a `comparison <#comparison>`__} "else" "end" -
   unindents or ends entire statements
-  control flow statement based on logic; after saying one of the above
   commands, you can use others command inside of it
-  example inputs: "if comparison variable x equals variable y", "elif
   variable x is greater than variable y", "else"
-  example outputs: ``if x == y:``, ``elif x > y:``, ``else:``

For
'''

-  structure: "for" {variable name} "in" {say an iterable `data
   type <#data-types>`__ and a value} "end" - unindents or ends entire
   statement
-  control flow statement that iterates over a data type; after using
   the command, you can use other commands inside of it
-  example inputs: "for i in list one cut two cut three", "for i in
   function range params one hundred"
-  example outputs: ``for i in [1, 2, 3]:``, ``for i in range(100)``

While
'''''

-  structure: "while comparison"(comparison is optional) {say a
   `comparison <#comparison>`__} "end" - unindents or ends entire
   statement
-  control flow statement that will continue while a condition is true;
   after using this command, you can use other commands inside of it
-  example inputs: "while comparison i is less than one hundred", "while
   true"
-  example outputs: ``while i < 100:``, ``while True:``

Define
''''''

-  structure: "define function"(function is optional) {say a name for
   the function} "parameters variable"(variable is optional) {say a name
   for the parameter} "cut" ...
-  used to allow users to define their own functions; after using this
   command, you can use other commands inside of it
-  example inputs: "define function fibonacci parameters variable
   number", "define factorial params number"
-  example outputs: ``def fibonacci(number):``,
   ``def factorial(number):``

Return
''''''

-  structure: "return" {say a `data type <#data-types>`__ and a value}
-  returns data from a function; can only be used in functions
-  example inputs: "return variable x", "return false"
-  example outputs: ``return x``, ``return False``

Data Types
~~~~~~~~~~

Integer\*
'''''''''

-  any whole number
-  structure: "integer"(optional) {say any whole number}
-  example inputs: "integer one", "twelve", "one hundred forty two"
-  example outputs: ``1``,\ ``12``, ``142``

String\*
''''''''

-  any piece of text; is iterable
-  structure: "string"(optional) {say anything}
-  example inputs: "string hello comma world exclamation point",
   "space", "if you're reading this it's too late"
-  example outputs: ``"hello, world!"``, ``" "``,
   ``"if you're reading this it's too late"``

Float\*
'''''''

-  a decimal number
-  structure: "float"(optional) {say any decimal}
-  example inputs: "float one point two", "three point one four one five
   nine"
-  example outputs: ``1.2``, ``3.14159``

Boolean\*
'''''''''

-  stores data as true or false
-  structure: "boolean"(optional) {either "true" or "false"}
-  example inputs: "boolean true", "false"
-  example outputs: ``True``, ``False``

Variable\*\*
''''''''''''

-  stores data types
-  structure: "variable"(sometimes optional) {any name}
-  example inputs: "variable x", "variable hello world", "i"
-  example outputs: ``x``, ``hello_world``, ``i``

Module\*\*
''''''''''

-  allows you to use functions and methods from different Python files (note: always used with a method)
-  stucture: "module method" {method name}
-  example inputs: "module math method factorial parameters ten", "module web browser method open params URL"
-  example outputs: ``math.factorial(10)``, ``webbrowser.open(url)``

Equation
''''''''

-  for math and simple string concatenation
-  structure: "equation" {say a `data type <#data-types>`__ and a value}
   {say an `equation operator <#equation-operators>`__ {say a `data
   type <#data-types>`__ and a value} ...
-  example inputs: "equation one plus five", "equation 12 times 4 plus
   3", "equation 6 mod 5"
-  example outputs: ``1 + 5``, ``12 * 4  + 3``, ``6 % 5``

Comparison
''''''''''

-  for comparing different Python objects
-  structure: "comparison" {say a `data type <#data-types>`__ and a
   value} {say a `comparison operator <#comparison-operators>`__} {say a
   `data type <#data-types>`__ and a value} ...
-  example inputs: "comparison variable x is True", "comparison ten is
   greater than twenty five", "comparison five is less than seven and
   ten is greater than nine"
-  example outputs: ``x is True``, ``10 > 25``, ``5 < 7 and 10 > 9``

List
''''

-  ordered group of different Python objects; is iterable
-  structure: "list" {say a `data type <#data-types>`__} {say a value}
   "cut" {say a `data type <#data-types>`__ and a value} ...
-  example inputs: "list", "list one cut two cut three", "list hello cut
   one point five"
-  example outputs: ``[]``, ``[1, 2, 3]``, ``["hello", 1.5]``

Tuple
'''''

-  immutable sequence of Python objects
-  structure: "tuple" {say a `data type <#data-types>`__} {say a value}
   "cut" {say a `data type <#data-types>`__ and a value} ...
-  example inputs: "tuple", "tuple one cut two cut three", "tuple hello"
-  example outputs: ``()``, ``(1, 2, 3)``, ``("hello",)``

Set
'''

-  group of unordered, unique Python objects
-  structure: "set" {say a `data type <#data-types>`__ and a value}
   "cut" {say a `data type <#data-types>`__} {say a value} ...
-  example inputs: "set", "set one cut one cut three", "set hello cut
   one point five"
-  example outputs: ``set()``, ``{1, 3}``, ``{"hello", 1.5}``

Function
''''''''

-  blocks of code that can perform action on parameters; when naming a
   builtin function, you can say what a shorthand name actually means;
   ie: "integer" -> ``int()``, "length" -> ``len()``, "has attribute" ->
   ``hasattr()``
-  structure: "function" {say a function name} "parameters" {say a `data
   type <#data-types>`__ and a value} cut ...
-  example inputs: "function list parameters hello", "function int
   params string ten"
-  example outputs: ``list("hello")``, ``int("10")``

\*Doesn't have be said when using this data type in a command; ie: you
can just say "one" instead of "integer one" to get the result of ``1``.

\*\*\ `"Variable" <#variable>`__ doesn't have to be said if the variable
has been defined, is being used as a parameter in a `function <#function>`__ or `method <#methods>`__, or is the variable in a `for loop <#for>`__. `"Module" <#module>`__ doesn't have to be said if the module is already imported.

Other Things
~~~~~~~~~~~~

Methods
'''''''

-  blocks of code that are called on class instances to perform actions
-  structure: {say a `data type <#data-types>`__ and a value} "method"
   {say a method name} "parameters" {say a `data type <#data-types>`__
   and a value} cut ...
-  example inputs: "variable x method append parameters one", "space
   method join params function list params hello"
-  example outputs: ``x.append(1)``, ``" ".join(list("hello"))``

Keywords
''''''''

-  "exit" - exits the program
-  "cancel" - cancels a multiline statement without exiting the program
-  "end" - unindents or ends a `for loop <#for>`__, `while loop <#while>`__, `function definition <#define>`__, or `if/elif/else statement <#if-elif-else>`__

Equation Operators
''''''''''''''''''

-  for use in equations
-  ``+`` - "plus"
-  ``-`` - "minus"
-  ``*`` - "times", "multiplied by"
-  ``/`` - "divided by"
-  ``**`` - "to the power of"
-  ``%`` - "mod", "modulus"

Comparison Operators
''''''''''''''''''''

-  for use in comparison expressions
-  ``==`` - "equals", "is equal to"
-  ``!=`` - "does not equal", "is not equal to"
-  ``>`` - "is greater than"
-  ``<`` - "is less than"
-  ``>=`` - "is greater than or equal to"
-  ``<=`` - "is less than or equal to"
-  Key words
-  ``and``
-  ``or``
-  ``is``
-  ``not``
-  ``in``

Shorthand words
'''''''''''''''

-  "params" can be used in place of "parameters"
