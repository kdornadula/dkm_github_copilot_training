"""
Exercise 1: Basic Function Writing with GitHub Copilot

OBJECTIVE: Practice writing clear, descriptive function names and comments
that help GitHub Copilot generate accurate code suggestions.

INSTRUCTIONS:
1. Read each TODO comment
2. Write a descriptive function name and docstring
3. Let GitHub Copilot suggest the implementation
4. Test the function with the provided examples
5. Refine if necessary

Remember: The key to good Copilot suggestions is clear intent!
"""

# TODO: Create a function that calculates the Body Mass Index (BMI)
# BMI = weight (kg) / height (m)^2
# The function should take weight in kg and height in meters
# Example: calculate_bmi(70, 1.75) should return approximately 22.86

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI) using weight and height.
    
    Args:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters
        
    Returns:
        float: BMI value
    """
    # Let Copilot suggest the implementation here
    pass


# TODO: Create a function that determines if a year is a leap year
# A leap year is divisible by 4, except for years divisible by 100
# unless they are also divisible by 400
# Example: is_leap_year(2024) should return True

def is_leap_year(year: int) -> bool:
    """
    Determine if a given year is a leap year.
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if leap year, False otherwise
    """
    # Let Copilot suggest the implementation here
    pass


# TODO: Create a function that converts a decimal number to binary
# The function should return a string representation of the binary number
# Example: decimal_to_binary(10) should return "1010"

def decimal_to_binary(decimal_num: int) -> str:
    """
    Convert a decimal number to its binary representation.
    
    Args:
        decimal_num (int): The decimal number to convert
        
    Returns:
        str: Binary representation as a string
    """
    # Let Copilot suggest the implementation here
    pass


# TODO: Create a function that finds the second largest number in a list
# If there are duplicate largest numbers, return the largest
# If list has less than 2 elements, return None
# Example: find_second_largest([1, 3, 4, 4, 2]) should return 3

def find_second_largest(numbers: list) -> int:
    """
    Find the second largest number in a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int: Second largest number, or None if not possible
    """
    # Let Copilot suggest the implementation here
    pass


# TODO: Create a function that generates a simple password
# Password should contain uppercase, lowercase, numbers
# Length should be configurable (default 8 characters)
# Example: generate_simple_password(12) should return a 12-character password

def generate_simple_password(length: int = 8) -> str:
    """
    Generate a simple password with mixed case letters and numbers.
    
    Args:
        length (int): Length of password (default 8)
        
    Returns:
        str: Generated password
    """
    # Let Copilot suggest the implementation here
    pass


# TODO: Create a function that calculates compound interest
# Formula: A = P(1 + r/n)^(nt)
# Where A = final amount, P = principal, r = annual rate, n = compounds per year, t = time in years
# Example: calculate_compound_interest(1000, 0.05, 4, 5) for $1000 at 5% compounded quarterly for 5 years

def calculate_compound_interest(principal: float, annual_rate: float, compounds_per_year: int, years: int) -> float:
    """
    Calculate compound interest using the standard formula.
    
    Args:
        principal (float): Initial amount of money
        annual_rate (float): Annual interest rate (as decimal, e.g., 0.05 for 5%)
        compounds_per_year (int): Number of times interest is compounded per year
        years (int): Number of years
        
    Returns:
        float: Final amount after compound interest
    """
    # Let Copilot suggest the implementation here
    pass


# Testing section - uncomment and run to test your implementations
if __name__ == "__main__":
    # Test BMI calculation
    # print(f"BMI for 70kg, 1.75m: {calculate_bmi(70, 1.75):.2f}")
    
    # Test leap year
    # print(f"Is 2024 a leap year? {is_leap_year(2024)}")
    # print(f"Is 1900 a leap year? {is_leap_year(1900)}")
    # print(f"Is 2000 a leap year? {is_leap_year(2000)}")
    
    # Test decimal to binary
    # print(f"10 in binary: {decimal_to_binary(10)}")
    # print(f"255 in binary: {decimal_to_binary(255)}")
    
    # Test second largest
    # print(f"Second largest in [1, 3, 4, 4, 2]: {find_second_largest([1, 3, 4, 4, 2])}")
    
    # Test password generation
    # print(f"Generated password: {generate_simple_password(12)}")
    
    # Test compound interest
    # print(f"Compound interest: ${calculate_compound_interest(1000, 0.05, 4, 5):.2f}")
    
    print("Uncomment the test cases above to test your implementations!")


"""
REFLECTION QUESTIONS:
1. Which function names and comments led to the best Copilot suggestions?
2. Did you need to modify any of Copilot's suggestions? Why?
3. How did the specificity of your comments affect the quality of suggestions?
4. What patterns did you notice in effective prompting?

NEXT STEPS:
- Try implementing these same functions in JavaScript
- Add error handling to make the functions more robust
- Write unit tests for each function
- Experiment with different comment styles and see how Copilot responds
"""