class Other(object):
        def override(self):
           print "Other override()"

        def implicite(self):
            print "Other implicit()"

        def altered(self):
            print "Other altered()"

class Child(object):
            def __init__(self):
             self.other=Other()

            def implicite(self):
              self.other.implicite()

            def override(self):
              print "Child override"

            def altered(self):
               print "Child,before other altered()"
               self.other.altered()
               print "Child,after other altered()"
son=Child()
son.implicite()
son.override()
son.altered()
