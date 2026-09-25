def is_palindrome(text):
    # Keep only letters and digits, ignore case
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

# Examples
print(is_palindrome("racecar"))                         # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("hello"))                           # False
print(is_palindrome(12321 and str(12321)))              # True