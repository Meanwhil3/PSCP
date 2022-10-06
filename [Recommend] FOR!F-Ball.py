"""[Recommend] FOR!F-Ball"""

def main():
    """[Recommend] FOR!F-Ball"""
    name = input()
    pos = 1
    for i in name:
        if i == "A" and pos == 1:
            pos = 2
        elif i == "A" and pos == 2:
            pos = 1
        elif i == "B" and pos == 2:
            pos = 3
        elif i == "B" and pos == 3:
            pos = 2
        elif i == "C" and pos == 1:
            pos = 3
        elif i == "C" and pos == 3:
            pos = 1
    print(pos)
main()
