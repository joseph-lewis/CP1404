"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    message = check_scores(score)
    print(message)


def check_scores(score):
    if score < 0:
        value = "Invalid score"
    elif score > 100:
        value = "Invalid score"
    elif score >= 90:
        value = "Excellent"
    elif score >= 50:
        value = "Passable"
    else:
        value = "Bad"
    return value


main()
