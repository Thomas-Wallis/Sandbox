MIN_LENGTH = 4
MAX_LENGTH = 10


password = input("Enter password here: ")
while MIN_LENGTH > len(password) or MAX_LENGTH < len(password):
    print("password must be {} to {} characters".format(MIN_LENGTH, MAX_LENGTH))
    password = input("Enter password here: ")
for character in password:
    print("*", end=' ')