"""[Recommend] RockPaperScissor"""
def check(naia, naib):
    """check"""
    ans = ""
    if naia == naib:
        ans = ""
    elif naia == "P" and naib == "R":
        ans = "A"
    elif naia == "R" and naib == "S":
        ans = "A"
    elif naia == "S" and naib == "P":
        ans = "A"
    else:
        ans = "B"
    return ans

def main():
    """[Recommend] RockPaperScissor"""
    name = input()
    total = ""
    for i in range(len(name)-1):
        if i % 2 == 0:
            total += check(name[i], name[i+1])
    total_a = total.count("A")
    total_b = total.count("B")
    if total_a == total_b:
        print("DRAW %d" %total_a)
    elif total_a > total_b:
        print("A win %d-%d" %(total_a, total_b))
    elif total_a < total_b:
        print("B win %d-%d" %(total_b, total_a))
main()
