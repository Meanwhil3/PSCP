"""Lotto"""

def main():
    """Lotto"""
    num1 = input()
    num2 = input()
    num3 = input()
    num4 = input()
    num5 = input()
    num6 = input()
    name = input()
    total = 0
    if name == num1:
        total += 6000000
    if name[-2:] == num2:
        total += 2000
    if name[:3] == num3 and name[:3] == num4:
        total += 8000
    elif name[:3] == num3 or name[:3] == num4:
        total += 4000
    if name[-3:] == num5 and name[-3:] == num6:
        total += 8000
    elif name[-3:] == num5 or name[-3:] == num6:
        total += 4000
    if num1 == "000000" and (name == "999999" or name == "000001"):
        total += 100000
    elif num1 == "999999" and name == "000000":
        total += 100000
    elif int(num1) - 1 == int(name) or int(num1) + 1 == int(name):
        total += 100000
    else:
        total = total
    print(total)
main()
