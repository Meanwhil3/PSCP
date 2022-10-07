"""Kaprekar"""

def check(num):
    """check"""
    total = []
    for i in num:
        total.append(int(i))
    name = []
    cal = ""
    while total:
        tal = total[0]
        for i in total:
            if i < tal:
                tal = i
        name.append(tal)
        total.remove(tal)
    for i in name:
        cal += str(i)
    return cal

def main():
    """Kaprekar"""
    num = input()
    suck = 1
    while num != "6174":
        if num == "6174":
            print(suck)
            break
        if len(str(num)) < 4:
            num = num + "0"
        else:
            total = check(num)[::-1]
            number = int(total) - int(total[::-1])
            if number == 6174:
                print(suck)
                break
            else:
                num = str(number)
                suck = suck + 1
main()
