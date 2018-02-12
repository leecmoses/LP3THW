# ==== I Choose... You! ====
from sys import exit

ready = []

def table():
    print("- There are three PokeBalls on the table.")
    print("Prof. Oak: Which one do you choose?")
    print(" 1. Bulbasaur.\n 2. Charmandar.\n 3: Squirtle.\n 4: Pikachu?")

    choice = input("> ")

    print("Pro. Oak: Are you sure?")
    print(" 1: Yes.\n 2: No.")

    choice_2 = input("> ")

    if choice == "1" and choice_2 == "1":
        print("Prof. Oak: Bulbasaur, it is! Congratulations on your first Pokemon!!")
        exit(0)
    elif choice == "2" and choice_2 == "1":
        print("Prof. Oak: Charmandar, it is! Congratulations on your first Pokemon!!")
        exit(0)
    elif choice == "3" and choice_2 == "1":
        print("Prof. Oak: Squirtle, it is! Congratulations on your first Pokemon!!")
        exit(0)
    elif choice == "4" and choice_2 == "1":
        print("Prof. Oak: I have to warn you. This Pikachu is a little troublesome...")
        print("- Pikachu stares at trainer, waiting for trainer's answer.")
        print("Pikachu: Pika-pika. Chu?")
        print("Prof. Oak: I will ask once more. Are you sure you want THIS Pikachu?")
        print(" 1: Yes.\n 2: No.")

        choice = input("> ")

        if choice == "1":
            print("- You embrace Pikachu with an endearing hug.")
            print("Pikachu: Pika?... PIKAAAA-CHUUUUU!")
            print("- Pikachu used Thundershock. The two of you are going to be good pals.")
            exit(0)
        elif choice == "2":
            print("- Pikachu begins to cry.")
            blackout("- Pikachu used Thunderbolt.")
        else:
            print("Prof. Oak: I see you are not ready to be a trainer. Then you cannot have a Pokemon.")
            blackout("- Trainer is devastated and absolutely heartbroken.") 
    else:
        print("Prof. Oak: I see you are not ready to be a trainer. Then you cannot have a Pokemon.")
        blackout("- Trainer is devastated and absolutely heartbroken.")

def lab():
    print("- Professor Oak is here waiting for you.")
    print("- You greet the professor.")
    if ready[0] == "yes":
        print("Prof. Oak: Good morning! Are you ready to choose your first Pokemon?")
        print(" 1: Yes, I am ready to choose my Pokemon.\n 2: No, not yet.\n 3: What is a Pokemon?")

        choice = input("> ")

        if choice == "1":
            print("Prof. Oak: Okay, select a Pokemon.")
            table()
        elif choice == "2":
            blackout("- While trainer tries to decide, three days pass by.")
        elif choice == "3":
            print("- The professor stares and is in dismay by your ignorance.")
            blackout("- Professor Oak used Firepunch! It's super effective!")
        else:
            blackout("- Trainer is confused.")
        
    elif ready[0] == "no":
        print("Prof. Oak: Officer Jenny! Please arrest this naked trainer!!")
        blackout("- Officer Jenny tasers you.")
    else:
        exit(0)

def blackout(how):
    print(how, "\n- You blacked out! You mysteriously lost ¥1,260!")
    exit(0)

def start():
    print("Trainer: Zzz... zzz...")
    print("Mom: Wake up, honey. You don't want to be late. Today is the big day.")
    print(" 1: Wake up.\n 2: Sleep in.")

    choice = input("> ")

    if choice == "1":
        print("- Trainer gets ready and goes downstairs.")
        print("Mom: Good, you're awake. You should head over to Professor Oak's lap. Errr... I meant lab!")
        print("- Trainer heads for the laboratory while pondering about the father that is never around.")
        ready.append("yes")
        lab()
    elif choice == "2":
        print("- Trainer falls back asleep...")
        print("Mom: Wake up now! You're late!!")
        print("Trainer: !!!")
        print("- Trainer panics and runs out the door barely clothed.")
        print("- Trainer enters the laboratory.")
        ready.append("no")
        lab()
    else:
        blackout("- ...")

start()