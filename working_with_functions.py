def multiply(number1, number2):
    """This functions multiplies two numbers."""
    return number1 * number2


def add(number1, number2):
    """This function adds two numbers."""
    return number1 + number2


def divide(number1, number2):
    """This function dived one number from another."""
    return number1 / number2


def calculate_area(width, height):
    """This function calculates the area of a rectangle."""
    return width * height


result = multiply(50, 20)          # This line executes the multiply function and store the result in 'result' variable
result1 = add(10, 20)
result2 = divide(50, 5)
result3 = calculate_area(500, 100)

print(result)
print(result1)
print(result2)
print(result3)
