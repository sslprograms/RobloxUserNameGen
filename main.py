import requests, threading, random

def check():
    try:
        users = ""
        for x in range(20):
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'l', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 1, 2, 3, 4, 5, 6, 7, 8 ,9]
            users = users + str(random.choice(letters))
        print(users)
        username = requests.get(f'https://auth.roblox.com/v1/usernames/validate?birthday=2006-09-21T07:00:00.000Z&context=Signup&username={users}')
        if username.json()['message'] == "Username is valid":
            with open('checked.txt', 'a') as usernames:
                usernames.write(users + '\n')
    except:
        pass

while True:
    threading.Thread(target=check,).start() 
