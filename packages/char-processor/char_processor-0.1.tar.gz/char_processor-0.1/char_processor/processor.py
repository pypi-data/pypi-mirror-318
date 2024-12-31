# char_processor/processor.py
def reverse_string(s):
    """Return the reverse of the input string."""
    return s[::-1]

def count_char(s, char):
    """Return the number of occurrences of char in the string s."""
    return s.count(char)

def is_palindrome(s):
    """Check if the string s is a palindrome."""
    return s == reverse_string(s)