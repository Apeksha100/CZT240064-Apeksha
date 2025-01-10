def is_palindrome(s):
    # Remove spaces and convert to lowercase to ignore case and spaces
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        return True
    else:
        return False

testS = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(testS):
    print(f"'{testS}' is a palindrome.")
else:
    print(f"'{testS}' is not a palindrome.")
