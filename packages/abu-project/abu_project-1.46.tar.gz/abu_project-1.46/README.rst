Project Title
=============

This is very simple package that comes with the following functionalities.

1. ``multiplication_table()`` : Prints the multiplication table from 1 to 5 by default.
2. ``fahrenheit_to_celsius()`` : Converts Fahrenheit to Celsius given an integer parameter.
3. ``celsius_to_fahrenheit()`` : Converts Celsius to Fahrenheit given an integer parameter.
4. ``finds_the_longest_word()`` : Returns the longest word from a provided string.
5. ``binary_to_decimal()`` : This function handles user input and output. It prompts the user to input a binary number, processes it through the ``main()`` function, and displays the appropriate result based on the validity of the input.
6. ``fibonacci_series_generator()`` : This function generates Fibonacci numbers interactively in groups of 10, allowing the user to proceed by pressing "Enter" or terminate the program with "Ctrl+D".

Documentation
-------------

See the documentation section at:

- `github <https://github.com/abuawaish/awaish_pkg>`_

Author
------

See the Author of this project at:

- `abuawaish7 <https://www.github.com/abuawaish>`_

Badges
------

abu-project

.. image:: https://badge.fury.io/py/abu-project.svg
    :target: https://pypi.org/project/abu-project/

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT

Installation and Use
--------------------

To install the package, use pip:

.. code:: sh

    pip install abu-project

To use the package in your Python script:

Usage
=====

To use the package in your Python script, first import the `FunnyFuncs` class from the `abu_project` module. Here are some examples:

.. code-block:: python

    from abu_project import FunnyFuncs

    funcs = FunnyFuncs()

    # Generate multiplication tables from 1 to 5
    funcs.multiplication_table()

    # Convert Fahrenheit to Celsius
    print(funcs.fahrenheit_to_celsius(440))  # Output: 440° Fahrenheit -> 226.67° Celsius

    # Convert Celsius to Fahrenheit
    print(funcs.celsius_to_fahrenheit(40))  # Output: 40° Celsius -> 104.00° Fahrenheit

    # Find the longest word in a sentence
    print(funcs.finds_the_longest_word("The quick brown fox jumps over the lazy dog"))
    # Output: The longest word is : jumps

    # Convert a binary number to decimal
    funcs.binary_to_decimal()

    # Generate Fibonacci numbers
    funcs.fibonacci_series_generator()


Features
========

1. **Multiplication Table**:
   Generate multiplication tables for a range of numbers.

2. **Temperature Conversion**:
   Convert temperatures between Fahrenheit and Celsius.

3. **Longest Word Finder**:
   Identify the longest word in a given sentence.

4. **Binary to Decimal Conversion**:
   Convert a binary number to its decimal equivalent.

5. **Fibonacci Series Generator**:
   Generate an infinite series of Fibonacci numbers.

License
=======

This project is licensed under the MIT License. See the LICENSE file for details.
