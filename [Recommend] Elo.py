"""[Recommend] Elo"""

def main():
    """[Recommend] Elo"""
    rate_a = int(input())
    rate_b = int(input())
    win = input().upper()
    ers_a = 1/(1+(10**((rate_b-rate_a)/400)))
    ers_b = 1/(1+(10**((rate_a-rate_b)/400)))
    if win == "A":
        print("%.2f" %ers_a)
    elif win == "B":
        print("%.2f" %ers_b)
main()
