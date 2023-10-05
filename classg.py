class Greeter:
    def __init__(self, name):
        self.name=name
    def greet(self,loud=False):
        if loud:
            print("HELLO",self.name.upper())
        else:
            print("HELLO",self.name.lower())
g=Greeter('Fred')
g.greet()
g.greet(loud=True)
