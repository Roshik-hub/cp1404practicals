"""
Emails Program
Estimate: 25 minutes
"""

def extract_name(email):
    """Extract a name from the email before the '@' symbol"""
    name_part = email.split('@')[0]
    name_parts = name_part.split('.')
    name = ' '.join(name_parts).title()
    return name

# Dictionary to store emails and names
email_to_name = {}

# Ask the user for the first email
email = input("Email: ")

# Keep looping until the user enters a blank email
while email != "":
    suggested_name = extract_name(email)
    response = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()

    if response == "n":
        name = input("Name: ")
    else:
        name = suggested_name

    email_to_name[email] = name

    # Ask for the next email
    email = input("Email: ")

# Print all emails and names
print()
for email, name in email_to_name.items():
    print(f"{name} ({email})")
