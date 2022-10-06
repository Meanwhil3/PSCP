"""Timing"""

def main():
    """Timing"""
    sec = int(input())
    day = sec//86400
    sec = sec-(86400*day)
    hour = sec//3600
    sec = sec-(3600*hour)
    minute = sec//60
    sec = sec-(60*minute)
    print(day, hour, minute, sec)
main()
