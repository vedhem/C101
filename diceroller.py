import random;
yn = input("would you like to roll a dice?")
while yn == "yes":
    num = random.randint(1,6)
    if num == 1:
        print(" ┌─────────┐\n",
              "│         │\n",
              "│    ●    │\n",
              "│         │\n",
              "└─────────┘")
        yn = input(("would you like to continue rolling?"))
        if yn == "no":
            break
    if num == 2:
        print(
        " ┌─────────┐\n",
        "│  ●      │\n",
        "│         │\n",
        "│      ●  │\n",
        "└─────────┘",)
        yn = input(("would you like to continue rolling?"))
        if yn == "no":
            break
    if num == 3:
        print(
        " ┌─────────┐\n",
        "│  ●      │\n",
        "│    ●    │\n",
        "│      ●  │\n",
        "└─────────┘",)
        yn = input(("would you like to continue rolling?"))
        if yn == "no":
            break
    if num == 4:
        print(
        " ┌─────────┐\n",
        "│  ●   ●  │\n",
        "│         │\n",
        "│  ●   ●  │\n",
        "└─────────┘",)
        yn = input(("would you like to continue rolling?"))
        if yn == "no":
            break
    if num == 5:
        print(
        " ┌─────────┐\n",
        "│  ●   ●  │\n",
        "│    ●    │\n",
        "│  ●   ●  │\n",
        "└─────────┘",)
        yn = input(("would you like to continue rolling?"))
        if yn == "no":
            break
    if num == 6:
        print(
        " ┌─────────┐\n",
        "│  ●   ●  │\n",
        "│  ●   ●  │\n",
        "│  ●   ●  │\n",
        "└─────────┘",)
        yn = input(("would you like to continue rolling?"))
        if yn == "no":
            break


    
