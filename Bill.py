"""Bill"""

def serve(num):
    """serve"""
    total = num*10/100
    if total < 50:
        num += 50
    elif total > 1000:
        num += 1000
    else:
        num += total
    return num

def main(bill):
    """Bill"""
    total_serve = serve(bill)
    total_serve += total_serve*7/100
    print("%.2f" %total_serve)
main(float(input()))
