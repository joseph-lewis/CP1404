"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
for state in STATE_NAMES:
    print("{:<3} is {}".format(state, STATE_NAMES[state]))

state_abbreviation = input("Enter short state: ")
while state_abbreviation != "":
    if state_abbreviation.upper() in STATE_NAMES:
        print(state_abbreviation.upper(), "is", STATE_NAMES[state_abbreviation.upper()])
    else:
        print("Invalid short state")
    state_abbreviation = input("Enter short state: ")

#Updating to feedback branch
