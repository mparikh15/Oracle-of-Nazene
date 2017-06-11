from sys import exit

#has_key = False

name = "NULL"

def large_chamber():
    print "\nAs you walk into the new chamber, the doors behind you lock... "
    raw_input(" ")
    print "This is a large, mostly empty room and there are two doors"
    raw_input(" ")
    print "You move to the middle of the room and look to the north and west"
    raw_input(" ")
    print "The door to the north has a large lock on it with an engraving of a"
    print "a winged horse monster. You know that this is called the Hippocampus."
    raw_input(" ")
    print "You do not know why you know about the Hippocampus, you just do."
    raw_input(" ")
    print "The door to the west is a simple wooden door, but a foul stench lies behind it..."
    raw_input(" ")
    door_choice(False)


def door_choice(key):
    holder = key
    print "\nYou return to the middle of the large chamber"
    raw_input(" ")
    print "What do you choose to do?"
    lcchoice = raw_input("> ")
    lcchoice = lcchoice.upper()

    if "WEST" in lcchoice:
        spike_chamber()

    elif "NORTH" in lcchoice and not key:
        print "You try to open the door, but it's locked!"
        raw_input(" ")
        print "You look closer at the lock, and it has a winged horse monster on it."
        raw_input(" ")
        print "There must be a key somewhere in the dungeon..."
        raw_input(" ")
        door_choice(False)

    elif "NORTH" in lcchoice and key:
        gold_room()

    elif "NAVI" in lcchoice:
        print "Navi doesn't have any useful suggestions here."
        door_choice(key)

    else:
        print "That's not really an option."
        door_choice(key)


def spike_chamber():
    print "\nYou are in a room that is filled with spikes."
    raw_input(" ")
    print "Vague deja vu hits you, you've been here before."
    raw_input(" ")
    print "While you can see that the room is split in two, this side has a direct"
    print "and safe path into the spikes."
    raw_input(" ")
    print "There's a door on the other side that's blocked by the spikes. You suspect it"
    print "leads back to the room where you first woke up. No need to go there again."
    raw_input(" ")
    print "There's a shiny object in the middle of the rusty spikes."
    spike_choice()


def spike_choice():
    print "\nDo you want to go towards the object?"
    choice = raw_input("> ")
    choice = choice.upper()

    if "YES" in choice or "Y" in choice:
        print "You walk forward through the spikes. Carefully..."
        raw_input(" ")
        print "You get to the middle of the spikes and look down."
        raw_input(" ")
        print "There's a key. It's very large and heavy, but you pick it up."
        raw_input(" ")
        print "After looking at it, you decide it's worth taking. You put it in your pocket."

        door_choice(True)

    elif "NO" in choice or "N" in choice:
        print "You decide not to go towards the object and head back to the previous room."
        door_choice()

    else:
        print "Don't ignore the question, %s YES or NO??\n" % name
        spike_choice()


def spike_chamber_front():
    print "\nYou walk into a poorly lit room."
    raw_input(" ")
    print "You realize that there's a huge array of spikes in front of you."
    raw_input(" ")
    print "You look more closely and see something shiny in the middle..."
    raw_input(" ")
    print "Unfortunately it's completely blocked off by spikes and there isn't\n"
    print "any good way of getting over to it. Maybe Navi can help?"
    raw_input(" ")
    spike_test()


def spike_test():
    print "\nWhat do you do?"
    choice = raw_input("> ")
    choice = choice.upper()

    if "NAVI" in choice:
        print "Navi flies over to take a closer look."
        raw_input(" ")
        print "She reports back, 'It looks like a key of some sort."
        raw_input(" ")
        print "It has a winged seamonster symbol on it."
        raw_input(" ")
        print "Unfortunately it's blocked by all of those spikes...'"
        raw_input(" ")
        print "Navi doesn't think you'll be able to reach it from this side of the room."
        raw_input(" ")
        print "She suggests you head BACK."
        spike_test()

    elif "BACK" in choice:
        print "You head back."
        first_room()

    elif "SPIKE" in choice or "JUMP" in choice or "LOOK" in choice:
        dead("That was a bad idea. You end up falling on a spike and dying.")

    else:
        print "That's not really an option..."
        spike_test()


def gold_room():
    print "You walk into a cavernous room with a foul smell."
    raw_input(" ")
    print "There are torches near the wall where you entered, but the way forward is dark."
    raw_input(" ")
    print "You hear a low grumbling noise coming from the darkness..."
    raw_input(" ")

    while True:
        print "What do you want to do now?\n"
        choice = raw_input("> ")
        choice = choice.upper()

        if "TORCH" in choice or "LIGHT" in choice:
            print "You take a torch off the wall and walk forward into the darkness.\n"
            darkness_w_torch()

        elif "STRAIGHT" in choice or "WALK" in choice or "FORWARD" in choice:
            print "You stumble around a bit, but find yourself lost. You head back towards the door and the TORCHES.\n"

        elif "NAVI" in choice:
            print "Well, we have a few options. We can WALK FORWARD into the darkness."
            raw_input(" ")
            print "We could also EXPLORE a bit."
            raw_input(" ")
            print "Whatever you end up doing, I think I'll stay here by the TORCHES where I can see.\n"
            raw_input(" ")

        elif "EXPLORE" in choice:
            print "You look around for a bit, mostly sweeping the area by the TORCHES"
            raw_input(" ")
            print "But you don't have much luck. You find a penny in the corner, but it was"
            print "face down, so you left it. No bad luck for %s!\n" % name
            raw_input(" ")

        else:
            print "That's not really an option here."


def darkness_w_torch():
    print "You win.. for now!"
    exit()



def dead(why):
    print why
    exit(0)


def dark_hallway():
    print "\nYou enter the door on the right and step into a large, dark hallway."
    raw_input(" ")
    print "You take a few steps forward and hear a voice."
    raw_input(" ")
    print "'HALT' shouts the voice."
    raw_input(" ")
    print "Ahead of you you see a frail old man."
    raw_input(" ")
    print "I've been waiting for you %s he cackles." % name
    raw_input(" ")
    print "To progress you must answer this riddle:"
    raw_input(" ")
    print "'It is greater than God; it is more evil than the devil; the poor have it;"
    print "the rich need it; and if you eat it, you will die. What is it?'"
    raw_input(" ")
    riddle_one()


def riddle_one():
    print "\nWhat do you want to do/guess?"
    guess = raw_input("> ")
    guess = guess.upper()

    if "NOTHING" in guess:
        print "'Very good! Very good indeed. Says the old man."
        raw_input(" ")
        print "'You may progress. Good luck.'"
        raw_input(" ")
        print "The old man disappears. You look around and cannot find him anwhere."
        raw_input(" ")
        print "You go up to the door at the other end of the chamber and it opens...\n"
        large_chamber()

    elif "BACK" in guess:
        print "You decide this isn't worth your time.\n"
        first_room()

    elif "NAVI" in guess:
        print "'I'm not really sure,' says Navi. 'I can't figure this one out."
        raw_input(" ")
        print "There's not much that the poor have that the rich don't. It's almost opposite.'"
        raw_input(" ")
        print "Navi pauses and thinks, if you can't figure it out, we could always FIGHT him.\n"
        riddle_one()

    elif "FIGHT" in guess:
        print "You yell at the old man and run towards him to fight."
        raw_input(" ")
        print "He laughs a bit under his breath and as you draw close, you realize"
        print "That he's not actually there. You look around, but can't find him."
        raw_input(" ")
        print "You walk forward to the door, but it won't open."
        raw_input(" ")
        print "There's no lock, but seems sealed too tightly..."
        raw_input(" ")
        print "There's no way forward along this path, so you head back.\n"
        first_room()

    else:
        print "Nope, that's not right! The old man laughs.\n"
        riddle_one()


def long_hallway():
    print "\nYou step into a long hallway. You can tell that nobody has been in this room \n"
    print "for years."
    raw_input(" ")
    print "It is well lit and the floor is made out of bricks and many are missing or loose."
    raw_input(" ")
    print "You step forward and notice a pile of BONES on the LEFT."
    raw_input(" ")
    print "On the RIGHT you see a PUDDLE of dark still water where a chunk of bricks are missing."
    raw_input(" ")
    print "You see something shiny in the middle of the puddle."
    raw_input(" ")
    print "At the end of the hallways is a DOOR that you can barely see.\n"
    middle_path()


def middle_path():
    global pole
    pole = False
    small_key = False

    while True:
        print "\nWhat do you do?"
        choice = raw_input("> ")
        choice = choice.upper()
        print pole

        if "DOOR" in choice and not small_key:
            print "You walk over towards the door at the far end of the hallway, but you realize"
            print "as you get near that the door is shut tight and that there's a keyhole in the middle."
            raw_input(" ")
            print "You know you need to keep looking around..."
            raw_input(" ")

        elif "DOOR" in choice and small_key:
            print "You open the door with the key. It's tough at first because of age, but the lock works fine."
            raw_input(" ")
            print "The door clicks open."
            raw_input(" ")
            print "You leave behind the pole because it's all but fallen apart at this point. You walk into the new room."
            large_chamber()

        elif pole and "PUDDLE" in choice or "RIGHT" in choice or "WATER" in choice:
            print "You use the wooden part of the spear you found to dig up the shiny object."
            raw_input(" ")
            print "It's dark and far down, so it takes you a few tries, but you"
            print "eventually pull up a small key on a string. This might open the door!"
            raw_input(" ")
            print "Unfortunately the spear has more or less fallen apart. Don't think it'll be useful anymore."
            small_key = True

        elif "PUDDLE" in choice or "RIGHT" in choice or "WATER" in choice and not pole:
            print "You walk over to the puddle on the right, but realize that the water is really deep."
            raw_input(" ")
            print "There's no way you can reach it by yourself, but there seems to be a string tied around it."
            raw_input(" ")
            print "Maybe if you can find a something to use as a pole..."
            raw_input(" ")


        elif "BONES" in choice or "LEFT" in choice:
            print "You walk over to the bones. It looks like he may have been a soldier once."
            raw_input(" ")
            print "That was many years ago though, clearly, and the armor and shield have all rusted compeltely."
            raw_input(" ")
            print "There's an old spear that looks usable though, do you want to take it? "
            take = raw_input("> ")
            take = take.upper()

            if "YES" in take or "Y" in take:
                print "You pick up the spear. As soon as you pick it up, the sharp metal part at the end crumbles."
                raw_input(" ")
                print "Not ideal, but at least you have a pole now."
                pole = True
                print pole

            else:
                print "You leave the spear there."

        else:
            print "That's not an option ", name


def start():
    global name
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "Oww... You wake up in a dark room. Your head hurts and you can't remember how you got here."
    raw_input(" ")
    print "You hear a voice, it introduces itself..."
    raw_input(" ")
    print "'Hello old friend', it says. 'My name is Navi and I am here to help.'"
    raw_input(" ")
    print "It looks like you hurt your head, do you remember your name?"
    choice = raw_input("> ")
    choice = choice.upper()


    if "YES" in choice or choice == "Y":
        print "'Okay great, you remember your name then, right? And it is:'\n"
        name = raw_input("> ")

        print "Okay, %s I'm glad your remeber your name." % (name)
        return name and navi_talk()


    elif "NO" in choice or choice == "N":
        print "'You don't remember anything huh? Well, your name is Zeke.'\n"
        name = "Zeke"
        return name and navi_talk()

    else:
        print "'You're incoherent, so I'm guessing you don't remember your name. It's Zeke.\n"
        name = "Zeke"
        return name and navi_talk()

#name = start()

def navi_talk():
    print "Now that we have that sorted, just a reminder that I can be helpful to you."
    raw_input(" ")
    print "When you're in a place and don't know what to do, I may be able to help."
    raw_input(" ")
    print "I'm also small and can take a closer look at things you cannot reach."
    raw_input(" ")
    print "To call me, just type NAVI."
    raw_input(" ")
    print "Here %s try it, just to see if you can do it right!\n" % name
    test()

def test():
    choice = raw_input("> ")
    choice = choice.upper()

    if "NAVI" in choice:
        print "Good, glad we got that out of the way. Now, we should move."
        raw_input(" ")
        print "Not a good idea to stay here too long."
        raw_input(" ")
        starting_room()

    else:
        print "Nope, that's not quite right, try again!"
        test()

def starting_room():
    print "\nYou look around this room."
    raw_input(" ")
    print "There are two doors here, one to the left and one to the right."
    raw_input(" ")
    print "In between those two doors is a long wall with seemingly nothing there..."
    raw_input(" ")
    print "Do you want to go through the door on the left or the door on the right?\n"

    door = raw_input("> ")
    door = door.upper()

    if "LEFT" in door:
        spike_chamber_front()

    elif "RIGHT" in door:
        dark_hallway()

    else:
        print "Navi rolls her eyes at your inability to decide. She picks a door for you."
        raw_input(" ")
        print "You end up going through the door on the RIGHT."
        dark_hallway()


def first_room():
    print "\nYou are in the first room again. You notice that the large gap in the middle now has a door in the middle."
    raw_input(" ")
    print "It strikes you as odd. The door wasn't there the first time you were in this room, but it's clearly there now."
    raw_input(" ")
    print "Oh well you have a choice now."
    three_choices()

def three_choices():
    print "\nWhich way do you want to go? LEFT, RIGHT or STRAIGHT."
    door = raw_input("> ")
    door = door.upper()

    if "LEFT" in door:
        spike_chamber_front()
    elif "STRAIGHT" in door:
        long_hallway()
    elif "RIGHT" in door:
        dark_hallway()
    else:
        print "%s is not an option" % (door)
        three_choices()

    #print "Cheat code time for testing!!"
    #choice_2 = raw_input("> ")

        #if choice_2 == 1:
        #    large_chamber()
        #else:
        #    large_chamber()


start()
