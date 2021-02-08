import os

os.system('cls')

print("\t\t EMAIL SLICER\n")
print("\tEnter your email and get\n\ta username and a domain that match.\n")

email = input("Enter your email: ")
print('\n')
emailInList = list(email)

usernameInList = []

i = 0
for x in emailInList:
    if emailInList[i] != "@":
        usernameInList.append(emailInList[i])
    elif emailInList[i] == "@":
        break
    i += 1

domainInList = []

y = len(email) - 1
for x in emailInList:
    if emailInList[y] != "@":
        domainInList.insert(0, emailInList[y])
    elif emailInList[y] == "@":
        break
    y -= 1

username = ''.join(map(str, usernameInList))  
print("Your perfect username is:", username)

print('\n')

domain = ''.join(map(str, domainInList))  
print("Your perfect domain is:", domain)