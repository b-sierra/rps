import random

def run():
    while True:
        select = ["rock", "paper", "scissors"]
        uinput = input("Rock, Paper, or Scissors? (or type 'quit'):")
        cinput = random.choice(select)
        match = [uinput + cinput]

        if uinput in select:
            print(f"{uinput} | {cinput}")
        elif uinput.lower() == "quit":
            break
        else:
            print("Invalid input.")

        def rockLogic():
            if match == ["rockscissors"]:
                match_R = "W"
                print(match_R)
            elif match == ["rockrock"]:
                match_R = "TIE"
                print(match_R)
            elif match == ["rockpaper"]:
                match_R = "L"
                print(match_R)

        def paperLogic():
            if match == ["paperrock"]:
                match_R = "W"
                print(match_R)
            elif match == ["paperpaper"]:
                match_R = "TIE"
                print(match_R)
            elif match == ["paperscissors"]:
                match_R = "L"
                print(match_R)

        def scissorsLogic():
            if match == ["scissorspaper"]:
                match_R = "W"
                print(match_R)
            if match == ["scissorsscissors"]:
                match_R = "TIE"
                print(match_R)
            if match == ["scissorsrock"]:
                match_R = "L"
                print(match_R)

        rockLogic()
        paperLogic()
        scissorsLogic()

run()

