
import requests, threading, random, string, sys

# if sys.argv[1] == "help":

thread_amount = 2

try:
    thread_amount = int(sys.argv[1]) #.index("--threadamount")
except:
    pass




characters = string.ascii_letters + string.digits # + "_"
run = True

def check(thread_num):
    global run

    print(f"Started thread #{thread_num}.")

    while run:
        try:
            new_username = ""
            for _ in range(random.randrange(10, 20)):
                new_username = new_username + random.choice(characters)
            
            msg = f"{thread_num} generated -> {new_username} "

            username = requests.get(f'https://auth.roblox.com/v1/usernames/validate?birthday=2006-09-21T07:00:00.000Z&context=Signup&username={new_username}')
            if username.json()['message'] == "Username is valid":
                with open('checked.txt', 'a') as usernames:
                    print(msg + "[Valid]")
                    usernames.write(new_username + '\n')
            else:
                print(msg + "[Taken]")
        except Exception as e:
            print(f"Thread #{thread_num} Error -> {e}")
    print(f"Thread #{thread_num} stopped.")

print(f"[Main] starting {thread_amount} threads...")
threads = []
for _ in range(thread_amount):
    t = threading.Thread(target=check, args=(_, ))
    t.start()
    threads.append(t)

try:
    while True:
        pass
except:
    run = False
    for t in threads:
        t.join() # wait for threads to stop
    print("[Main] stopped.")