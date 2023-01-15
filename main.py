import os
import template
import json
import re

template = template.template
def create_file(farm, player_command, action):
    output = template.replace("player", player_command).replace("action", action)
    with open(os.path.join('scripts' , f"{farm}.sc"), "w") as f:
        f.write(output)


def check_alphanumeric_underscore(string):
    if re.match("[a-zA-Z0-9_]", string):
        return True
    else:
        return False

with open("whitelist.json", "r") as file:
    whitelist = json.load(file)

restart = True
while restart == True:
    farm = input("What is the name of the farm? \n \n(Note: this will be the /command)\n")
    while check_alphanumeric_underscore(farm) is False:
        print(f"{farm} contains invalid characters!")
        farm = input("What is the name of the farm? \n \n(Note: this will be the /command)\n")
        farm = farm.replace(" ", "_")
    farm = farm.replace(" ", "_")
    player_command = input("What is the command used to spawn the player?\n")
    parts = player_command.split(" ")
    player = parts[1][0:]
    command = parts[0].replace("/","")
    print(command)
    while any(d["name"].lower() == player.lower() for d in whitelist) or "/" not in player_command or parts[2] != "spawn" or command != "player":
        if any(d["name"].lower() == player.lower() for d in whitelist):
            print(f"ERROR: {player} is on the whitelist!")
        elif "/" not in player_command:
            print("ERROR: '/' is required.")
        elif parts[2] != "spawn":
            print("ERROR: Command requires 'spawn'.")
        elif command != "player":
            print("ERROR: Must use a /player command.\n")
        player_command = input("What is the command used to spawn the player?\n")
        parts = player_command.split(" ")
        player = parts[1][0:]
        player = player
        command = parts[0].replace("/","")
    action_command = input("What is the action command?\n")
    while player not in action_command or "/" not in action_command:
        print("Action command must contain a forward slash '/' and the player must be the same for both commands!")
        action_command = input("What is the action command?\n")

    preview = input(f"Are you sure you want to create a script that runs {player_command} and {action_command} called {farm}.sc? 'yes' to continue or 'no' to restart. ")
    if preview == "yes":
        create_file(farm, player_command, action_command)
        os.system('clear')
        redo = input("Would you like to try again? 'yes' or 'no'. ")
        if redo == "no":
            restart = False
            os.system('clear')
        if redo == "yes":
            os.system('clear')
    elif preview == "no":
        os.system('clear')
        redo = input("Would you like to try again? 'yes' or 'no'. ")
        if redo == "no":
            restart = False
            os.system('clear')
        if redo == "yes":
            os.system('clear')