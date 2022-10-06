"""BigFrame"""

def main():
    """BigFrame"""
    word_1 = input().rstrip().lstrip()
    word_2 = input().rstrip().lstrip()
    word_3 = input().rstrip().lstrip()
    word_4 = input().rstrip().lstrip()
    word_5 = input().rstrip().lstrip()
    most_len = 0
    if len(word_1) >= len(word_2) and len(word_1) >= len(word_3) and\
len(word_1) >= len(word_4) and len(word_1) >= len(word_5):
        most_len = len(word_1)
    elif len(word_2) >= len(word_1) and len(word_2) >= len(word_3) and\
len(word_2) >= len(word_4) and len(word_2) >= len(word_5):
        most_len = len(word_2)
    elif len(word_3) >= len(word_1) and len(word_3) >= len(word_2) and\
len(word_3) >= len(word_4) and len(word_3) >= len(word_5):
        most_len = len(word_3)
    elif len(word_4) >= len(word_1) and len(word_4) >= len(word_2) and\
len(word_4) >= len(word_3) and len(word_4) >= len(word_5):
        most_len = len(word_4)
    elif len(word_5) >= len(word_1) and len(word_5) >= len(word_2) and\
len(word_5) >= len(word_3) and len(word_5) >= len(word_4):
        most_len = len(word_5)
    ms_ms = most_len+4
    print("*"*ms_ms)
    print("* "+word_1+" "*(ms_ms-3-len(word_1))+"*")
    print("* "+word_2+" "*(ms_ms-3-len(word_2))+"*")
    print("* "+word_3+" "*(ms_ms-3-len(word_3))+"*")
    print("* "+word_4+" "*(ms_ms-3-len(word_4))+"*")
    print("* "+word_5+" "*(ms_ms-3-len(word_5))+"*")
    print("*"*ms_ms)
main()
