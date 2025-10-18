"""
CP1404/CP5632 Practical
"""
COLOUR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Beige": "#f5f5dc",
    "Coral": "#ff7f50",
    "Crimson": "#dc143c",
    "Gold": "#ffd700",
    "Indigo": "#4b0082",
    "Lavender": "#e6e6fa",
    "LightGreen": "#90ee90"
}

# Repeatedly ask user for a colour name
colour_name = input("Enter a colour name: ").title()

while colour_name != "":
    try:
        print(f"The code for {colour_name} is {COLOUR_CODES[colour_name]}")
    except KeyError:
        print("Invalid colour name.")
    colour_name = input("Enter a colour name: ").title()

print("Goodbye!")
