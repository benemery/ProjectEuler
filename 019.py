#!/usr/bin/python
import datetime

def count_sundays(start_date, end_date):
    answer = 0
    sunday = start_date + datetime.timedelta(days=6 - start_date.weekday())
    one_week = datetime.timedelta(days=7)

    if sunday.day == 1:
        answer += 1
    while sunday < end_date:
        sunday += one_week
        if sunday.day == 1:
            answer += 1
    return answer

def test():
    # No test
    return True

def main():
    return count_sundays(datetime.date(1901, 1, 1), datetime.date(2000, 12, 31))

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()