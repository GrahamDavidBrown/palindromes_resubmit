import re


def is_palindrome(user_in):
    user_in = re.sub(r'\W+', '', user_in).lower()
    while len(user_in) > 1:
        if user_in[0] == user_in[-1]:
            print(user_in[1:-1])
            return is_palindrome(user_in[1:-1])
        else:
            return False
    return True


if is_palindrome(re.sub(r'\W+', '', input("Enter a palindrome, or don't: ")).lower()):
    print('Yes, palindrome')
else:
    print('No, not palindrome')
