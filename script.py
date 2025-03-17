class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof Woof")

class Owner:
    def __init__(self,name,address,contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number


owner1 = Owner("Ranit","Kolkata","1234567890")
dog1 = Dog("Kalu","Desi Kutta",owner1)
print(dog1.name)
print(dog1.breed)
print(dog1.owner.name)

dog1.name = "tommy"
print(dog1.name)
print(dog1.breed)
dog1.bark()

