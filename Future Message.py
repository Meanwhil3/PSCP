"""Future Message"""

def main(num):
    """Future Message"""
    if num.isnumeric():
        print("Number")
    elif num.isupper():
        print("Uppercase")
    elif num.islower():
        print("Lowercase")
    elif num.istitle():
        print("Title")
    elif num.isspace():
        print("Space")
    else:
        print("Other")
main(input())
