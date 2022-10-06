"""GraderMachine"""
def wowo():
    """GraderMachine"""
    total = 0
    ans = ""
    first = int(input())
    last = int(input())
    for i in range(first, last+1):
        if i % 2 == 0 and i != 0:
            total += i
            ans += ("%s " %i)
    if last < first:
        for i in range(first, last-1, -1):
            if i % 2 == 0 and i != 0:
                total += i
                ans += ("%s " %i)
    print("pass : %s" %ans, end="")
    print()
    print("Sum : %d" %total)
wowo()
