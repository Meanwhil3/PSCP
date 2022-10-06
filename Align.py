"""Align"""

def main():
    """Align"""
    long = int(input())
    where = input()
    name = input()
    total_name = len(name)
    total_long = long-total_name
    suck_cen = total_long // 2
    wt_suck = total_long - suck_cen
    if long >= total_name:
        if where == "center":
            if wt_suck > suck_cen:
                print((" "*(suck_cen+1))+name+(" "*suck_cen))
            else:
                print(name.center(long))
        elif where == "left":
            print(str(name)+((" ")*total_long))
        else:
            print((" "*total_long)+"%s" %name)
main()
