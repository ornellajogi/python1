### NOT DONE
"""
Write a password strength verifier in Python that checks if user password is strong.
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.


password = 'food'
result = False

password = '1EggPerD@y'
result = True
"""

def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # Python3 program to check if a given
    # password is strong or not.
    def printStrongNess(input_string):

        n = len(input_string)

        # Checking lower alphabet in string
        hasLower = False
        hasUpper = False
        hasDigit = False
        specialChar = False
        normalChars = "abcdefghijklmnopqrstu"
        "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "

        for i in range(n):
            if input_string[i].islower():
                hasLower = True
            if input_string[i].isupper():
                hasUpper = True
            if input_string[i].isdigit():
                hasDigit = True
            if input_string[i] not in normalChars:
                specialChar = True

        # Strength of password
        print("Strength of password:-", end="")
        if (hasLower and hasUpper and
                hasDigit and specialChar and n >= 8):
            print("Strong")

        elif ((hasLower or hasUpper) and
              specialChar and n >= 6):
            print("Moderate")
        else:
            print("Weak")

    # Driver code
    if __name__ == "__main__":
        input_string = "GeeksforGeeks!@12"

        printStrongNess(input_string)

    # This code is contributed by Yash_R
