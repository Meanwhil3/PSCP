"""FourDirections"""

def main():
    """FourDirections"""
    name = input()
    name1 = ""
    name2 = ""
    name3 = ""
    name4 = ""
    name5 = ""
    for i in name:
        if i == "U":
            name1 += "  *   "
            name2 += " ***  "
            name3 += "* * * "
            name4 += "  *   "
            name5 += "  *   "
        elif i == "D":
            name1 += "  *   "
            name2 += "  *   "
            name3 += "* * * "
            name4 += " ***  "
            name5 += "  *   "
        elif i == "L":
            name1 += "  *   "
            name2 += " *    "
            name3 += "***** "
            name4 += " *    "
            name5 += "  *   "
        elif i == "R":
            name1 += "  *   "
            name2 += "   *  "
            name3 += "***** "
            name4 += "   *  "
            name5 += "  *   "
    print(name1)
    print(name2)
    print(name3)
    print(name4)
    print(name5)
main()
