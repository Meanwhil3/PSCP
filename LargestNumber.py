"""LargestNumber"""

def compare_number(value_1, value_2):
    """Compare number"""
    if value_1 > value_2:
        return value_1
    return value_2

def main():
    """Main function"""
    num1 = input()
    num2 = input()
    num3 = input()

    lastest = num1 + num2 + num3
    lastest = compare_number((num1 + num3 + num2), lastest)
    lastest = compare_number((num2 + num1 + num3), lastest)
    lastest = compare_number((num2 + num3 + num1), lastest)
    lastest = compare_number((num3 + num2 + num1), lastest)
    lastest = compare_number((num3 + num1 + num2), lastest)
    print(int(lastest))
main()
