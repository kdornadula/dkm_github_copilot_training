/**
 * Basic Functions - GitHub Copilot Training Examples
 * 
 * This file demonstrates how to write clear, descriptive function names
 * and comments that help GitHub Copilot generate better code suggestions.
 */

/**
 * Calculate the area of a circle given its radius
 * @param {number} radius - The radius of the circle
 * @returns {number} The area of the circle
 */
function calculateCircleArea(radius) {
    return Math.PI * radius ** 2;
}

/**
 * Convert temperature from Celsius to Fahrenheit
 * @param {number} celsius - Temperature in Celsius
 * @returns {number} Temperature in Fahrenheit
 */
function convertCelsiusToFahrenheit(celsius) {
    return (celsius * 9/5) + 32;
}

/**
 * Find the largest number in an array of numbers
 * @param {number[]} numbers - Array of numbers to search
 * @returns {number|null} The largest number, or null if array is empty
 */
function findLargestNumberInArray(numbers) {
    if (!numbers || numbers.length === 0) {
        return null;
    }
    return Math.max(...numbers);
}

/**
 * Count the frequency of each word in a given text
 * @param {string} text - The input text to analyze
 * @returns {Object} Object with words as keys and frequencies as values
 */
function countWordFrequency(text) {
    const words = text.toLowerCase()
        .replace(/[.,!?;:"]/g, '') // Remove punctuation
        .split(/\s+/)
        .filter(word => word.length > 0);
    
    const frequency = {};
    words.forEach(word => {
        frequency[word] = (frequency[word] || 0) + 1;
    });
    
    return frequency;
}

/**
 * Check if a string is a palindrome (reads the same forwards and backwards)
 * @param {string} text - The text to check
 * @returns {boolean} True if the text is a palindrome, false otherwise
 */
function isPalindrome(text) {
    const cleanedText = text.replace(/\s+/g, '').toLowerCase();
    return cleanedText === cleanedText.split('').reverse().join('');
}

/**
 * Calculate the factorial of a non-negative integer
 * @param {number} n - The number to calculate factorial for
 * @returns {number} The factorial of n
 * @throws {Error} If n is negative
 */
function calculateFactorial(n) {
    if (n < 0) {
        throw new Error('Factorial is not defined for negative numbers');
    }
    if (n === 0 || n === 1) {
        return 1;
    }
    return n * calculateFactorial(n - 1);
}

/**
 * Generate a Fibonacci sequence with the specified number of terms
 * @param {number} count - Number of Fibonacci numbers to generate
 * @returns {number[]} Array containing the Fibonacci sequence
 */
function generateFibonacciSequence(count) {
    if (count <= 0) return [];
    if (count === 1) return [0];
    if (count === 2) return [0, 1];
    
    const sequence = [0, 1];
    for (let i = 2; i < count; i++) {
        const nextNum = sequence[i-1] + sequence[i-2];
        sequence.push(nextNum);
    }
    
    return sequence;
}

/**
 * Validate if an email address has a basic valid format
 * @param {string} email - The email address to validate
 * @returns {boolean} True if email format is valid, false otherwise
 */
function validateEmailAddress(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

/**
 * Generate a random password with specified length and character types
 * @param {number} length - Length of the password
 * @param {Object} options - Options for character types to include
 * @param {boolean} options.includeUppercase - Include uppercase letters
 * @param {boolean} options.includeLowercase - Include lowercase letters  
 * @param {boolean} options.includeNumbers - Include numbers
 * @param {boolean} options.includeSymbols - Include symbols
 * @returns {string} Generated password
 */
function generateRandomPassword(length = 12, options = {}) {
    const {
        includeUppercase = true,
        includeLowercase = true,
        includeNumbers = true,
        includeSymbols = false
    } = options;
    
    let characters = '';
    if (includeUppercase) characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (includeLowercase) characters += 'abcdefghijklmnopqrstuvwxyz';
    if (includeNumbers) characters += '0123456789';
    if (includeSymbols) characters += '!@#$%^&*()_+-=[]{}|;:,.<>?';
    
    if (characters === '') {
        throw new Error('At least one character type must be included');
    }
    
    let password = '';
    for (let i = 0; i < length; i++) {
        password += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    
    return password;
}

/**
 * Format a number as currency
 * @param {number} amount - The amount to format
 * @param {string} currency - Currency code (default: 'USD')
 * @param {string} locale - Locale for formatting (default: 'en-US')
 * @returns {string} Formatted currency string
 */
function formatAsCurrency(amount, currency = 'USD', locale = 'en-US') {
    return new Intl.NumberFormat(locale, {
        style: 'currency',
        currency: currency
    }).format(amount);
}

// Example usage and testing
if (typeof window === 'undefined') { // Node.js environment
    console.log('Circle area (radius=5):', calculateCircleArea(5));
    console.log('25°C in Fahrenheit:', convertCelsiusToFahrenheit(25));
    console.log('Largest in [3, 1, 4, 1, 5]:', findLargestNumberInArray([3, 1, 4, 1, 5]));
    console.log('Word frequency in "hello world hello":', countWordFrequency("hello world hello"));
    console.log('Is "racecar" a palindrome?', isPalindrome("racecar"));
    console.log('Factorial of 5:', calculateFactorial(5));
    console.log('First 8 Fibonacci numbers:', generateFibonacciSequence(8));
    console.log('Is "test@example.com" valid email?', validateEmailAddress("test@example.com"));
    console.log('Random password:', generateRandomPassword(12, { includeSymbols: true }));
    console.log('Currency format:', formatAsCurrency(1234.56));
}

// Export functions for use in other modules (Node.js)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        calculateCircleArea,
        convertCelsiusToFahrenheit,
        findLargestNumberInArray,
        countWordFrequency,
        isPalindrome,
        calculateFactorial,
        generateFibonacciSequence,
        validateEmailAddress,
        generateRandomPassword,
        formatAsCurrency
    };
}