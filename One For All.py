"""One For All"""

def main():
    """One For All"""
    afo = int(input())
    names = ""
    for i in range(1, afo+1):
        name = input()
        if i < afo:
            if i%2 != 0:
                names += (name+("*"*i))
            elif i%2 == 0:
                names += (name+(("-"*i)))
        elif i == afo:
            names += name
    if afo > 0:
        print(str(names)+"_"+str(afo))
main()
