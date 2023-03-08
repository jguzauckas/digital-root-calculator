# Digital Root Calculator

A digital root is the result of iteratively summing the digits of a number until your result is only a single digit (in base 10, this would be 1 through 9).

This calculator allows the user to enter a number to check the digital root of. It will calculate the digital root for any positive number, but will note if the number is prime or not. When entering a negative number, it lets the user know the input is supposed to be positive. Any other input will result in the program exiting the loop.

The primality check is a basic loop that checks divisibility with every integer from 2 up to the floor of the square root of the number. It could be more efficient by only checking prime numbers within the same range, but for the purpose of this example, we will keep this form.
