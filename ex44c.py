class Parent(object):
    def altered(self):
        print "PaRENT altered()"
class Child(Parent):
    def altered(self):
        print "Child,Before parent altered()"
        super(Child,self).altered()
        print "Child,Afer parent altered()"
dad=Parent()
son=Child()
dad.altered()
son.altered()
