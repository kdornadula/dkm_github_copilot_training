"""
Data Structures - GitHub Copilot Training Examples

This file demonstrates working with various Python data structures
and how descriptive naming helps Copilot suggest better code.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Student:
    """Represents a student with basic information."""
    name: str
    age: int
    email: str
    grades: List[float]
    
    def calculate_average_grade(self) -> float:
        """Calculate the student's average grade."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def add_grade(self, grade: float) -> None:
        """Add a new grade to the student's record."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")


class Library:
    """A simple library management system."""
    
    def __init__(self):
        self.books: Dict[str, Dict[str, Any]] = {}
        self.borrowed_books: Dict[str, str] = {}  # book_id -> borrower_name
    
    def add_book(self, book_id: str, title: str, author: str, year: int) -> None:
        """Add a new book to the library."""
        self.books[book_id] = {
            "title": title,
            "author": author,
            "year": year,
            "available": True
        }
    
    def borrow_book(self, book_id: str, borrower_name: str) -> bool:
        """
        Borrow a book from the library.
        
        Returns:
            bool: True if book was successfully borrowed, False otherwise
        """
        if book_id in self.books and self.books[book_id]["available"]:
            self.books[book_id]["available"] = False
            self.borrowed_books[book_id] = borrower_name
            return True
        return False
    
    def return_book(self, book_id: str) -> bool:
        """
        Return a borrowed book to the library.
        
        Returns:
            bool: True if book was successfully returned, False otherwise
        """
        if book_id in self.borrowed_books:
            self.books[book_id]["available"] = True
            del self.borrowed_books[book_id]
            return True
        return False
    
    def search_books_by_author(self, author: str) -> List[Dict[str, Any]]:
        """Search for books by a specific author."""
        matching_books = []
        for book_id, book_info in self.books.items():
            if author.lower() in book_info["author"].lower():
                book_info_copy = book_info.copy()
                book_info_copy["id"] = book_id
                matching_books.append(book_info_copy)
        return matching_books


def create_shopping_cart() -> Dict[str, Dict[str, Any]]:
    """Create an empty shopping cart structure."""
    return {
        "items": {},
        "total": 0.0,
        "created_at": datetime.now().isoformat()
    }


def add_item_to_cart(cart: Dict[str, Any], item_name: str, price: float, quantity: int = 1) -> None:
    """
    Add an item to the shopping cart.
    
    Args:
        cart: The shopping cart dictionary
        item_name: Name of the item to add
        price: Price per unit of the item
        quantity: Number of items to add (default: 1)
    """
    if item_name in cart["items"]:
        cart["items"][item_name]["quantity"] += quantity
    else:
        cart["items"][item_name] = {
            "price": price,
            "quantity": quantity
        }
    
    # Update total
    cart["total"] = sum(
        item["price"] * item["quantity"] 
        for item in cart["items"].values()
    )


def filter_students_by_grade_average(students: List[Student], min_average: float) -> List[Student]:
    """
    Filter students who have an average grade above the minimum threshold.
    
    Args:
        students: List of Student objects
        min_average: Minimum average grade threshold
        
    Returns:
        List of students meeting the criteria
    """
    return [
        student for student in students 
        if student.calculate_average_grade() >= min_average
    ]


def group_items_by_category(items: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Group items by their category.
    
    Args:
        items: List of items, each with a 'category' key
        
    Returns:
        Dictionary where keys are categories and values are lists of items
    """
    grouped = {}
    for item in items:
        category = item.get("category", "uncategorized")
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item)
    return grouped


def merge_dictionaries_with_sum(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    """
    Merge two dictionaries, summing values for common keys.
    
    Args:
        dict1: First dictionary
        dict2: Second dictionary
        
    Returns:
        New dictionary with merged and summed values
    """
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result


def find_common_elements(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Find elements that appear in both lists.
    
    Args:
        list1: First list
        list2: Second list
        
    Returns:
        List of common elements (without duplicates)
    """
    return list(set(list1) & set(list2))


# Example usage and testing
if __name__ == "__main__":
    # Test Student class
    student1 = Student("Alice Johnson", 20, "alice@example.com", [85.5, 92.0, 78.5])
    print(f"Student: {student1.name}, Average: {student1.calculate_average_grade():.2f}")
    
    # Test Library class
    library = Library()
    library.add_book("001", "The Python Programming Language", "Guido van Rossum", 1991)
    library.add_book("002", "Clean Code", "Robert Martin", 2008)
    
    print(f"Borrowed book 001: {library.borrow_book('001', 'John Doe')}")
    print(f"Books by Robert Martin: {library.search_books_by_author('Robert Martin')}")
    
    # Test shopping cart
    cart = create_shopping_cart()
    add_item_to_cart(cart, "Apple", 1.50, 5)
    add_item_to_cart(cart, "Banana", 0.75, 3)
    print(f"Cart total: ${cart['total']:.2f}")
    
    # Test data processing functions
    items = [
        {"name": "Apple", "category": "fruit"},
        {"name": "Carrot", "category": "vegetable"},
        {"name": "Banana", "category": "fruit"}
    ]
    grouped = group_items_by_category(items)
    print(f"Grouped items: {grouped}")
    
    # Test dictionary merging
    sales_q1 = {"product_a": 100, "product_b": 150}
    sales_q2 = {"product_a": 120, "product_c": 200}
    total_sales = merge_dictionaries_with_sum(sales_q1, sales_q2)
    print(f"Total sales: {total_sales}")