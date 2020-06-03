# Non usable python code for demo purpose
# Import the modules
import sys
import random

ans = True

while ans:
    question = "Ask the magic 8 ball a question: (press enter to quit) "

    answers = random.randint(1, 8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print("It is certain")

def sortByVotes():
    url = "http://www.commandlinefu.com/commands/browse/sort-by-votes/json"

    #print json.dumps(response,indent=2)
    for c in range(5):
        print("-" * 60)
        print(c)

while True:
    answer = "What would you like to do? "

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

class MyNewClass:
    pass
