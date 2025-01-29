import pdb
def reverse_number(n):
    is_negative = n < 0  # Check if number is negative
    n = abs(n)  # Work with absolute value

    reversed_num = 0
    while n > 0:
        pdb.set_trace()
        digit = n % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Append digit to reversed number
        n //= 10  # Remove last digit

    return -reversed_num if is_negative else reversed_num  # Restore sign if negative

# Test cases
print(reverse_number(1234))   # Output: 4321
print(reverse_number(-5678))  # Output: -8765
print(reverse_number(0))      # Output: 0
print(reverse_number(100))    # Output: 1
print(reverse_number(-900))   # Output: -9