"""Turnstile"""

def main():
    """Turnstile"""
    coin = ""
    total = 0
    while True:
        name = input()
        if name == "END":
            break
        elif name == "C" and coin != "C":
            coin += name
        elif coin == "C":
            if name == "P":
                total += 1
                coin = ""
    print(total)
main()
