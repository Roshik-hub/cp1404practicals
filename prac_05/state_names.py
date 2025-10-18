"""
CP1404/CP5632 Practical
"""
STATE_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

print(STATE_NAMES)

state = input("Enter short state: ").upper()
try:
    print(f"{state} is {STATE_NAMES[state]}")
except KeyError:
    print("Invalid short state")

for abbr, name in STATE_NAMES.items():
    print(f"{abbr:3} is {name}")
