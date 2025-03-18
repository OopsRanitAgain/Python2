class PrivateClass:
    def __init__(self):
        self.public_data = 'I am Public data'
        self.__private_data = 'I am Private data'

my_object = PrivateClass()

#Accessing the Public Attribute
print(my_object.public_data) #Output: I am Public data

#Tryin to access the Private Attribute
try:
    print(my_object.__private_data) #Raises AttributeError
except AttributeError as e:
    print(e) #Output: 'PrivateClass' object has no attribute '__private_data'

#Accessing the Private Attribute using Name Mangling
print(my_object._PrivateClass__private_data) #Output: I am Private data
# The Private Attribute __private_data is accessible using Name Mangling
# The Name Mangling is done by adding the class name to the
# private attribute with an underscore prefix