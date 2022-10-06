# """[Recommend] Ball"""
# def check(val):
#     """check"""
#     ans = (val*3)/5
#     return ans

def main(num):
    """[Recommend] Ball"""
    total = num * 100
    ans_num = -1
    if num > 0.01:
        while total > 1:
            total = (total*3)/5
            ans_num += 1
        print(ans_num)
    else:
        print("0")
main(float(input()))
