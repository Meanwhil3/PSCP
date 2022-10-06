"""[Recommend] PhoneNumber"""
def phone_home(total_num, num, country):
    """phone_home"""
    if total_num == 9 and country == "Domestic":
        return print("0", num[1:5], num[5:])
    elif total_num == 9 and country == "International":
        return print("+66", num[1:5], num[5:])

def phone(total_num, num, country):
    """phone"""
    if total_num == 10 and country == "Domestic":
        return print("0"+num[1], num[2:6], num[6:])
    elif total_num == 10 and country == "International":
        return print("+66"+num[1], num[2:6], num[6:])

def main():
    """[Recommend] PhoneNumber"""
    num = input()
    country = input()
    total_num = len(num)
    phone_home(total_num, num, country)
    phone(total_num, num, country)
main()
        