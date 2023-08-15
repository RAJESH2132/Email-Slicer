# importing regular expression
import re

# Collecting email address from user
email = input("Enter an email address: ")

# Extracting UserName and Domain
match = re.match(r'(.+)@(.+)', email)

# checking email format
if match:
    username = match.group(1)
    domain = match.group(2)
else:
    print("Invalid Email Format.")
    exit()

# Checking Whether it common email provider
common_providers = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
if domain in common_providers:
    print("This is a common email provider.")
else:
    print("This might be a custom domain.")

# Displaying extracted username and domain
print("Username: ", username)
print("Domain: ", domain)
