# John Smith -> DairyFarm
# john.smith@dairyfarm.com.au

# Snake Case -> first_name -> python preferred for variables and functions
# Pascal Case -> FirstName -> preferred for class names
# Camel Case -> firstName -> javascript preferred for variables and functions
# Kebab Case -> first-name -> CSS preferred for variables

# Get first name from the user
first_name = input("Enter your first name: ")

# Get last name from the user
last_name = input("Enter your last name: ")

# Get the name of the company without space
company_name = input("Enter the name of the company without spaces: ")

# create the email format
email_format = (first_name + "." + last_name + "@" + company_name + ".com.au").lower()

email_format_fstring = f"{first_name}.{last_name}@{company_name}.com.au".lower()

# print that email
print(email_format)
print(email_format_fstring)