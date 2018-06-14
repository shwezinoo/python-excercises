class Parent(object):
    def override(self):
        print "PARENT override()"
    def implicit(self):
        print "PARENT implicit()"
    def altered(self):
        print "PARENT altered()"
class Child(Parent):
    def override(self):
        print "child overried"
    def altered(self):
        print "Child,Before parent altered"
        super(Child,self).altered()
        print "Child,after parent altered"
dad=Parent()
son=Child()
dad.implicit()
son.implicit()
dad.override()
son.override()
dad.altered()
son.altered()
