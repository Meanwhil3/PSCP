"""Triangle I"""

def main():
    """Triangle I"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num3:
        num1, num3 = num3, num1
    if num1 > num2:
        num1, num2 = num2, num1
    abc = (num2**2)+(num1**2)
    total = (abc**(1/2))
    if num3-0.01 == total or total == num3+0.01 or total == num3:
        print("Yes")
    else:
        print("No")
main()
