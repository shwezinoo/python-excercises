class Death(Scene):
    quips=[
            "You died.You kinds suck at this",
            "Your mom would be proud....if she were smarter",
            "Such a luser",
            "I have a small puppy that's better at this"
            ]
    def enter(self):
        print Death.quips[randint(0,len(self.quips)-1)]
        exit(1)

