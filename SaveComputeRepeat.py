"""SaveComputeRepeat"""

def main():
    """SaveComputeRepeat"""
    start_here = 492137954293754252786
    mili = start_here
    second = mili//1000
    mili = mili%1000
    minute = second//60
    second = second%60
    hour = minute//60
    minute = minute%60
    days = hour//24
    hour = hour%24
    print(days, hour, minute, second, mili, sep=" ")
main()
