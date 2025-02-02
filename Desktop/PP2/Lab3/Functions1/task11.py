def is_palindrome(s):
    #s = ''.join(s.split())
    return s == s[::-1]

print(is_palindrome("qazaq"))
print(is_palindrome("A man a plan a canal Panama"))
