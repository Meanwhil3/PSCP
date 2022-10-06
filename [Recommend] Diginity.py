"""[Recommend] Diginity"""

def main():
    """[Recommend] Diginity"""
    total = ""
    num = "123456789"
    suck = 0
    while True:
        name = input()
        if name != "0":
            if name in num:
                total += name
            else:
                for i in range(name):
                    suck += i
        elif name == "0":
            print(total)
            return
main()
