import requests, threading, random, string

def check():
    try:
        users = ""
        for x in range(20):
            letters = string.ancii_letters + string.digits + string.ancii_letters
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
