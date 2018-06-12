print "You enter a dark room with two door"
door=raw_input(">")
if door=="1":
    bear=raw_input(">")
    if bear=="1":
        print "The bear eat your face off"
    elif bear=="2":
        print "The bear eats your legs off"
    else:
        print "Well doing %s,Bear runs away"%bear
elif door=="2":
    insanity=raw_input(">")
    if insanity=="1" or insanity=="2":
        print "Your body survius.Good job"
    else:
        print "The insanity rots your eye into a pool"
else:
    print "You stumble.Good job"

