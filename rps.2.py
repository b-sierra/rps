import random
p1 = ["rock", "paper", "scissors"]
user_score = 0
cpu_score = 0

def logic(user, cpu):
    global user_score
    global cpu_score
    if cpu == user:
        print(f"{user} = {cpu}")
        print("Tie!")
    elif user == "rock" and cpu == "paper":
        print(f"{user} > {cpu}")
        print("L!")
        cpu_score += 1
    elif user == "rock" and cpu == "scissors":
        print(f"{user} < {cpu}")
        print("W!")
        user_score += 1
    elif user == "paper" and cpu == "rock":
        print(f"{user} < {cpu}")
        print("W!")
        user_score += 1
    elif user == "paper" and cpu == "scissors":
        print(f"{user} > {cpu}")
        print("L!")
        cpu_score += 1
    elif user == "scissors" and cpu == "rock":
        print(f"{user} > {cpu}")
        print("L!")
        cpu_score += 1
    elif user == "scissors" and cpu == "paper":
        print(f"{user} < {cpu}")
        print("W!")
        user_score += 1
    print(f"You: {user_score} | Vro: {cpu_score}")

def start():
    global user_score
    global cpu_score
    while True:
        user = input("Rock, Paper, Scissors? (type 'quit' to exit):")
        if user.upper() == 'QUIT':
            break
        cpu = random.choice(p1)
        if user in p1:
            print("Ro... Sham... BRO!")
            logic(user, cpu)
        else:
            print("Invalid input.")

start()
    

          