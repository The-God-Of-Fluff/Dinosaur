class Dinosaur:

    def __init__(self, name, species, diet):
        self.name = name 
        self.species = species 
        self.diet = diet 

    def rawr(self):
         print(f"{self.name} lets out a mighty raaaaaaaawwwrrr")

    def eat(self, food):
        if food == self.diet:
            print(f"{self.name} eats {food} . . . mmm . . . Delish. Uncle Roger agrees.")
        else:
            print(f"{self.name} doesnt eat {food} blehhh")
    def type(self):
        print(f"{self.name} is a {self.species}")




rex = Dinosaur("Steve", "Tyrannosaurus Rex", "meat") 

spike = Dinosaur("Spike", "Stegosaurus", "plants") 
george = Dinosaur("George", "Pteradoctyl", "everything") 

print(spike.name)

spike.rawr()
spike.type()
spike.eat("plants")

print(george.name)

george.rawr()
george.type()
george.eat("everything")

print(rex.name)

rex.rawr()
rex.type()
rex.eat("meat")