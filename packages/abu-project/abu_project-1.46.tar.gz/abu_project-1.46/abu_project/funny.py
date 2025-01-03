from typing import Generator

class FunnyFuncs:
    def multiplication_table(self, start: int = 1, end: int = 5) -> None:
        """
        Generates and prints multiplication tables for numbers within a specified range.

        Args:
            start (int, optional): The starting number for the multiplication table. Defaults to 1.
            end (int, optional): The ending number for the multiplication table. Defaults to 5.

        Returns:
            None: This function prints the multiplication tables directly to the console.
        """
        for i in range(start, end + 1):
            print(f'multiplication_table for {i} ↓\n')
            for j in range(1, 11):
                print(f'{i} * {j} : {i * j}')
            print()

    def fahrenheit_to_celsius(self, fahrenheit_temperatures: int | float) -> str:
        """
        Converts a temperature from Fahrenheit to Celsius.

        Args:
            fahrenheit_temperatures (int): The temperature in Fahrenheit to be converted.

        Returns:
            str: A formatted string showing the conversion from Fahrenheit to Celsius.
        """
        celsius = (fahrenheit_temperatures - 32) * 5 / 9
        return f'{fahrenheit_temperatures}° Fahrenheit -> {celsius:.2f}° Celsius'

    def celsius_to_fahrenheit(self, celsius: int | float) -> str:
        """
        Converts a temperature from Celsius to Fahrenheit.

        Args:
            celsius (int): The temperature in Celsius to be converted.

        Returns:
            str: A formatted string showing the conversion from Celsius to Fahrenheit.
        """
        fahrenheit = (celsius * 9 / 5) + 32
        return f'{celsius}° Celsius -> {fahrenheit:.2f}° Fahrenheit'

    def finds_the_longest_word(self, sentence: str) -> str:
        """
        Finds and returns the longest word in a given sentence.

        Args:
            sentence (str): A sentence from which to find the longest word.

        Returns:
            str: A string indicating the longest word found in the sentence.
        """
        longest_word: str = max(sentence.split(), key=len)
        return f'The longest word is : {longest_word}'

    def __main(self, num: int) -> int | str:
        """
        Converts a binary number to its decimal equivalent.

        Args:
            num (int): A positive binary number to be converted.

        Returns:
            int | str: The decimal equivalent of the binary number, or an error message if the input is invalid.
        """
        if num < 0:
            return "Please enter a positive binary number."
        boolean: bool = any(char in "23456789" for char in str(num))
        if boolean:
            return "Invalid binary number. Only 0 and 1 are allowed."
        binary, power = 0, 0
        while num != 0:
            last_digit = num % 10
            binary += last_digit * (2 ** power)
            num //= 10
            power += 1
        return binary

    def binary_to_decimal(self) -> None:
        """
        Prompts the user to input a binary number, converts it to decimal, and prints the result.

        Returns:
            None: This function prints the result or an error message directly to the console.
        """
        binary_number: int = int(input("Enter the Binary Number : "))
        result: int | str = self.__main(binary_number)  # type: ignore
        print(result if isinstance(result, str) else f"The decimal of {binary_number} is {result}")

    def __fibonacci_generator(self) -> Generator[int, None, None]:
        """
        A generator that yields Fibonacci numbers indefinitely.

        Yields:
            int: The next number in the Fibonacci sequence.
        """
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    def fibonacci_series_generator(self) -> None:
        """
        Continuously generates and prints Fibonacci numbers in groups of 10 until the user stops the program.

        Instructions:
            - Press "Enter" to generate the next 10 Fibonacci numbers.
            - To terminate the program, press "Ctrl+D".

        Returns:
            None: This function prints Fibonacci numbers directly to the console.
        """
        fib_gen: Generator[int, None, None] = self.__fibonacci_generator()
        n: int = 10
        line_break: str = "_" * 65
        print(line_break)
        print("Note --> if you want to stop the script, Please press \"Ctrl+D\"")
        print(line_break)
        try:
            while True:
                input(f'Tap "enter" for the next {n} Fibonacci numbers')
                print(line_break)
                for _ in range(n):
                    print(next(fib_gen))
                print(line_break)
        except EOFError:
            print("\nProgram terminated.")

