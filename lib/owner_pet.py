# lib/owner_pet.py

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Store pets privately

    def pets(self):
        """Return a full list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Add a pet to the owner."""
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added.")
        if pet not in self._pets:
            pet.owner = self  # Set the pet's owner
            self._pets.append(pet)

    def get_sorted_pets(self):
        """Return a sorted list of pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # List to store all pet instances

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type. Choose from: {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)  # Add instance to the all list
        if owner:
            owner.add_pet(self)  # Ensure that the owner is updated if provided
