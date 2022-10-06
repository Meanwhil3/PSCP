"""BMI"""

def cal_bmi(name, weight, tall):
    """BMI"""
    bmi = weight / ((tall/100)**2)
    print((name)+("'s BMI = %.2f" %bmi))

def main():
    """main"""
    name, name2, name3, name4, name5 = input(), input(), input(), input(), input()
    weight, weight2, weight3 = float(input()), float(input()), float(input())
    weight4, weight5 = float(input()), float(input())
    tall, tall2, tall3 = float(input()), float(input()), float(input())
    tall4, tall5 = float(input()), float(input())
    cal_bmi(name, weight, tall)
    cal_bmi(name2, weight2, tall2)
    cal_bmi(name3, weight3, tall3)
    cal_bmi(name4, weight4, tall4)
    cal_bmi(name5, weight5, tall5)
main()
    