# tests/test_processor.py
from char_processor import reverse_string, count_char, is_palindrome

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_count_char():
    assert count_char("hello", "l") == 2

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False