"""
Basic Functions - GitHub Copilot Training Examples

This file demonstrates how to write clear, descriptive function names
and comments that help GitHub Copilot generate better code suggestions.
"""

import math
from typing import List, Dict, Optional


def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle
    """
    return math.pi * radius ** 2


def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32


def find_largest_number_in_list(numbers: List[float]) -> Optional[float]:
    """
    Find the largest number in a list of numbers.
    
    Args:
        numbers (List[float]): List of numbers to search
        
    Returns:
        Optional[float]: The largest number, or None if list is empty
    """
    if not numbers:
        return None
    return max(numbers)


def count_word_frequency(text: str) -> Dict[str, int]:
    """
    Count the frequency of each word in a given text.
    
    Args:
        text (str): The input text to analyze
        
    Returns:
        Dict[str, int]: Dictionary with words as keys and frequencies as values
    """
    words = text.lower().split()
    frequency = {}
    for word in words:
        # Remove punctuation
        word = word.strip('.,!?;:"')
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    
    Args:
        text (str): The text to check
        
    Returns:
        bool: True if the text is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(' ', '').lower()
    return cleaned_text == cleaned_text[::-1]


def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)


def generate_fibonacci_sequence(count: int) -> List[int]:
    """
    Generate a Fibonacci sequence with the specified number of terms.
    
    Args:
        count (int): Number of Fibonacci numbers to generate
        
    Returns:
        List[int]: List containing the Fibonacci sequence
    """
    if count <= 0:
        return []
    elif count == 1:
        return [0]
    elif count == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, count):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    
    return sequence


def validate_email_address(email: str) -> bool:
    """
    Validate if an email address has a basic valid format.
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if email format is valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


# Example usage and testing
if __name__ == "__main__":
    # Test the functions
    print("Circle area (radius=5):", calculate_circle_area(5))
    print("25°C in Fahrenheit:", convert_celsius_to_fahrenheit(25))
    print("Largest in [3, 1, 4, 1, 5]:", find_largest_number_in_list([3, 1, 4, 1, 5]))
    print("Word frequency in 'hello world hello':", count_word_frequency("hello world hello"))
    print("Is 'racecar' a palindrome?", is_palindrome("racecar"))
    print("Factorial of 5:", calculate_factorial(5))
    print("First 8 Fibonacci numbers:", generate_fibonacci_sequence(8))
    print("Is 'test@example.com' valid email?", validate_email_address("test@example.com"))