'''
dict 
dictionary -- keys, values key->value 
term -> definition

list - ordered bucket of items
list indexing  indexing
'''
from random import shuffle

player_data = {"name": "Curly", "hit_points":10, "pocket_contents":None }
print(player_data)

choice = input(f"You wake up and realize your name is {player_data['name']} and you have\
 {player_data['hit_points']} hit points remaining.  There is a cave in front of you.\
\nWhat will you do? \n1)Run away or \n2)Enter the cave.")

if (choice == "1"):
    print("You ran away. The end.")
    exit()
else:
    print("You have entered the cave.  There is a lit torch by the entrance.\
In front of you there are three wooden chests.")
    chests = ["Tiny Porcupine", "Empty", "Trap Door"]
    shuffle(chests)
    #print(chests[0])
    #print(chests[1])
    #print(chests[2])
    choice = int(input("Choose a number 1-3.  Which chest will you open?"))-1
    if chests[choice]=="Tiny Porcupine":
        print("You open the chest.\nYou get stabbed by a tiny porcupine and you run away")
        player_data["hit_points"]-=1
        player_data["pocket_contents"] = "Porcupine Quill"
    elif chests[choice]=="Empty":
        print("The chest is empty. You are filled with disappointment and run away with nothing.")
    elif chests[choice] =="Trap Door":
        print("Good job! You found a gold nugget.  Under the nugget there is a trap door.  Your adventures have just begun.")
        player_data["pocket_contents"] = "Gold Nugget"
    else:
        print("You don't follow instructions very well.  You run away in frustration")

    print(f"The day is finished. You now have {player_data['hit_points']} hit points and in your pocket is {player_data['pocket_contents']}")
