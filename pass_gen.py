import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

# set password length
pwd_length = 12

# generate a password satisfying some constraints:
# should contain at least one special char;
# should contain at least two digits
while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    if (any(char in special_chars for char in pwd) and
            sum(char in digits for char in pwd) > 2):
        break

print(pwd)
