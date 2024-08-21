import re
a = str(input("Word:"))
def is_palindrome(s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]
result = is_palindrome(a)
print(result)  
