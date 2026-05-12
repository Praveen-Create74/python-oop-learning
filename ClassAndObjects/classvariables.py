class Pet:
    total_pets=1
    species="Dog"
    def __init__(self,name,species):
        self.name=name
        Pet.species=species
    def new(self,name,species):
        self.name=name
        self.species=species
        Pet.total_pets+=1
    def show(self):
        return self.name,self.species,Pet.total_pets
obj=Pet("Tommy","Dog")
print(obj.show())
print(Pet.species)
print(Pet.total_pets)