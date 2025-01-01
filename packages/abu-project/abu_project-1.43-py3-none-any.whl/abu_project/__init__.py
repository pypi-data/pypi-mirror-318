from typing import Generator


def multiplication_table(start: int = 1, end: int = 5) -> None:
    """
    This function generates a multiplication table for numbers within a specified range.
    
    :param start: The `start` parameter in the `multiplication_table` function specifies the starting
    number for which you want to generate the multiplication table. If no value is provided when calling
    the function, it defaults to 1, defaults to 1
    :type start: int (optional)
    :param end: The `end` parameter in the `multiplication_table` function represents the ending number
    for which you want to generate the multiplication table. The function will generate multiplication
    tables starting from 1 up to this specified `end` number, defaults to 5
    :type end: int (optional)
    """
    for i in range(start, end + 1):
        print(f'multiplication_table for {i} ↓')
        print()
        for j in range(1, 11):
            print(f'{i}*{j} : {i * j}')
        print()


def fahrenheit_to_celsius(fahrenheit_temperatures: int) -> str:
    """
    The function `fahrenheit_to_celsius` converts a temperature in Fahrenheit to Celsius and returns the
    result formatted to two decimal places.
    
    :param fahrenheit_temperatures: The parameter `fahrenheit_temperatures` represents the temperature
    in Fahrenheit that you want to convert to Celsius. You can pass a single integer value representing
    the temperature in Fahrenheit to the function `fahrenheit_to_celsius` to get the equivalent
    temperature in Celsius
    :type fahrenheit_temperatures: int
    :return: The function `fahrenheit_to_celsius` takes an integer input representing a temperature in
    Fahrenheit, converts it to Celsius, and returns a string that includes the original Fahrenheit
    temperature and the converted Celsius temperature with two decimal places.
    """
    celsius = (fahrenheit_temperatures - 32) * 5 / 9
    return f'Fahrenheit {fahrenheit_temperatures} -> Celsius : {celsius:.2f}'


def celsius_to_fahrenheit(celsius: int) -> str:
    """
    This Python function converts a temperature in Celsius to Fahrenheit and returns the result in a
    formatted string.
    
    :param celsius: The `celsius_to_fahrenheit` function takes a parameter `Celsius` which is an integer
    representing the temperature in Celsius that you want to convert to Fahrenheit
    :type celsius: int
    :return: The function `celsius_to_fahrenheit` returns a formatted string that includes the input
    Celsius temperature and the converted Fahrenheit temperature with two decimal places.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return f'Celsius {celsius} -> fahrenheit : {fahrenheit:.2f}'


def finds_the_longest_word(sentence: str) -> str:
    """
    This Python function takes a sentence as input and returns the longest word in the sentence.
    
    :param sentence: A string containing words from which you want to find the longest word
    :type sentence: str
    :return: The function `finds_the_longest_word` returns a string that states the longest word found
    in the input sentence.
    """
    longest_word = [word for word in sentence.split() if len(word) == len(max(sentence.split(), key=len))][0]
    return f'The longest word is : {longest_word}'


def __main(num: int) -> int | str:
    """
    The function `_main` converts a positive binary number to decimal, handling invalid inputs, and the
    function `binary_to_decimal` takes user input for a binary number and prints its decimal equivalent
    or an error message.

    :param num: The `num` parameter in the `_main` function represents the binary number input by the
    user. It is an integer value that is checked for validity and converted to decimal if it meets the
    criteria
    :type num: int
    :return: The `_main` function returns either an integer representing the decimal equivalent of a
    binary number inputted by the user, or a string message indicating if the input is invalid. The
    `binary_to_decimal` function takes user input for a binary number, calls the `_main` function to
    convert it to decimal, and then prints the result or an error message if the input is invalid.
    """
    if num < 0:
        return "Please enter a positive binary number."
    else:
        boolean: bool = any(char in "23456789" for char in str(num))
        if boolean:
            return "Invalid binary number. Only 0 and 1 are allowed."
        else:
            last_digit: int = 0
            binary: int = 0
            power: int = 0
            while num != 0:
                last_digit = num % 10
                binary = binary + (last_digit * 2 ** power)
                num = num // 10
                power += 1
            return binary
def binary_to_decimal() -> None:
    """
    The function `binary_to_decimal` converts a binary number inputted by the user into its decimal
    equivalent.
    """
    binary_number: int = int(input("Enter the Binary Number : "))
    result: int = __main(binary_number)  #type:ignore
    if isinstance(result, str):  # Check if the result is a message
        print(result)
    else:
        print(f"The decimal of {binary_number} is {result}")


def __fibonacci_generator(self) -> Generator[int, None, None]:
    self.a, self.b = 0, 1
    while True:
        yield self.a
        self.a, self.b = self.b, (self.a + self.b)
def fibonacci_series_generator(self) -> None:
    fib_gen: Generator[int, None, None] = self.__fibonacci_generator()
    n: int = 10
    line_break: str = "_" * 65
    print(line_break)
    print("Note --> if you want to stop the script, Please press \"ctrl+d\"")
    print(line_break)

    """
    Continuously generates and prints Fibonacci numbers in groups of `n` until the user stops the program.

    This method interacts with the user through the console, allowing them to generate the next set of 
    Fibonacci numbers by pressing "Enter." The user can terminate the script by pressing "Ctrl+D" (EOFError).

    Attributes:
        fib_gen (Generator[int, None, None]): An infinite generator producing Fibonacci numbers.
        n (int): The number of Fibonacci numbers displayed per iteration (default is 10).
        line_break (str): A separator string for visual clarity in the console output.

    Instructions:
        - Tap "Enter" to generate the next `n` Fibonacci numbers.
        - To stop the program, press "Ctrl+D" on the keyboard.

    Raises:
        EOFError: Triggered when the user inputs "Ctrl+D" to terminate the program.

    Returns:
        None
    """

    try:
        while True:
            input(f'Tap "enter" for the next {n} number of fibonacci')

            print(line_break)
            for i in range(n):
                print(f'{next(fib_gen)}')
            print(line_break)
    except EOFError:
        print("\nProgram terminated.")
        return
