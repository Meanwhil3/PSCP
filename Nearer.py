"""Nearer"""

def main(alice, bob, ice_cream):
    """Nearer"""
    alice = abs(alice-ice_cream)
    bob = abs(bob-ice_cream)
    if alice < bob:
        print("Alice %d" %alice)
    elif bob < alice:
        print("Bob %d" %bob)
    elif bob == alice:
        print("Sundaes %d" %bob)
main(int(input()), int(input()), int(input()))
