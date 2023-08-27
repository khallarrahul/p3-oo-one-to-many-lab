class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner

        if pet_type not in Pet.PET_TYPES:
            raise TypeError("Pet type must be valid")
        Pet.all.append(self)
        self.pet_type = pet_type


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet Class")
        pet.owner = self

    def get_sorted_pets(self):
        namelist = []
        objlist = []
        namelist = [pet.name for pet in Pet.all if pet.owner == self]
        namelist.sort()
        for name in namelist:
            for pet in Pet.all:
                if pet.name == name:
                    objlist.append(pet)
        return objlist
