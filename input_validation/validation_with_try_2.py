""" Class: CIS 189
Author: Alex Rickels
Module 3 Assignment: Basic Input and Format Output """

# Code works as expected, with try/except/else/finally block used appropriately.


def average(s1, s2, s3):
    if s1 < 0:
        raise ValueError
    elif s2 < 0:
        raise ValueError
    elif s3 < 0:
        raise ValueError
    else:
        total = float(s1 + s2 + s3)
        avg = float(total/3)
        return avg


if __name__ == '__main__':
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    age = input("How old are you?")
    score_1 = float(input("What was your first score?"))
    score_2 = float(input("What was your second score?"))
    score_3 = float(input("What was your third score?"))
    try:
        average_scores = average(score_1, score_2, score_3)
        print(last_name + ", " + first_name + " age: " + age + " average grade: " + str(average_scores))
    except ValueError:
        print("Value Error, no negatives")


# test 1: 85, 90, 95: expected: 90 PASS
# test 2: 91.2 92.5, 65.6 expected: 83.1: PASS
# test 3: 65.22, 76.33, 87.44 expected: 76.33
