from sys import exit

def gold_room():
    print "This room is full of gold"
    
    next=raw_input(">")
    if "0" in next or "1" in next:
        how_much=int(next)
    else:
        dead("Man,learn to type a number")
    if how_much <50:
        print "nice,you're not greed"
    else:
        dead("You greed bastard")
def bear_room():
    bear_moved=False

    while True:
        next=raw_input(">")

        if next=="take honey":
            dead("The bear look at you")
        elif next=="taunt bear" and not bear_moved:
            print "The bear moved from the door"
        elif next=="taunt bear" and bear_moved:
            dead("The bear gets pissed off")
        elif next=="open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what the means"

def cthulhu_room():

     next=raw_input(">")

     if "flee" in next:
         start()
     elif "head" in next:
         dead("Well that was tasty")
     else:
         cthulhu_room()
def dead(why):
    print why,"Good job"
    exit(0)

def start():
    if next=="left":
        bear_room()
    elif next=="right":
        cthulhu_room()
    else:
        dead("You stumbles around the room")
start()        
        
