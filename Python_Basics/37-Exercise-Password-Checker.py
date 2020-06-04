# Quick program that asks for username and password and then displays password length

username = input('Username: ')
password = input('Password: ')
hidden_password = '*' * len(password) #hiding password so it doesn't get displayed on screen, instead, a '*' for every character in the password string is going to be displayed

print(f'\n{username} \nYour password: {hidden_password} is {len(password)} characters long')