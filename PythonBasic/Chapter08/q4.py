import sys
def greet_users(usernames) :
    for name in usernames :
        print(f'Hello, {name.capitalize()}')

usernames = sys.argv[1:]

greet_users(usernames)

