import math

# Return primality of a number
def is_prime(num: int) -> bool:
    for i in range(2, int(math.sqrt(num))):  # Only need to check up to sqrt of number
        if num % i == 0:
            return False
    return True


# Return iteratively summed digits
def digit_sum(num: int) -> int:
    # Determine number of digits by finding maximum power of 10 that fits
    num_digits = 0
    while (
        10**num_digits <= num
    ):  # Check if current power is still less than the number
        num_digits += 1

    # Find the sum of digits by determining place value using powers of 10
    sum = 0
    for i in range(num_digits):
        place_value = num // 10 ** (
            num_digits - (i + 1)
        )  # Divide by current largest power
        sum += place_value
        num -= place_value * 10 ** (num_digits - (i + 1))  # Take away largest digit

    # Recursion to keep narrowing down to 1 digit
    if num_digits > 1:
        sum = digit_sum(sum)
    return sum


input_val = " "
while input_val != "":
    # Get input from user
    input_val = input(
        "Enter a positive number to check the digital root of or enter anything else to leave: "
    )

    try:
        input_num = int(input_val)
    except:
        break

    # Check for conditions before calculating digital root
    if input_num <= 0:
        print("This is not a positive number!\n")
    elif not is_prime(input_num):
        print(
            input_num,
            "is not a prime number, and its digital root is",
            str(digit_sum(input_num)) + ".\n",
        )
    else:
        print(
            input_num,
            "is a prime number, and its digital root is",
            str(digit_sum(input_num)) + ".\n",
        )
