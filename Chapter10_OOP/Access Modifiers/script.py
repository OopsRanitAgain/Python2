class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email # Protected attribute
        self.__password = password # Private attribute  
    
    def get_email(self):
        return self._email
    
    def clean_email(self):
        return self._email.lower().strip()
    
user1 = User('ranit','Ranit@example.com','123456')
print(user1._email)
print(user1.get_email())
print(user1.clean_email())

user1._email = 'john@example.com'
print(user1.get_email())
print(user1.clean_email())

#Why email is made Protected

#Protected attributes are those attributes that are intended to be used only within the class or its subclasses.
#Protected attributes are prefixed with a single underscore (_).
#Protected attributes are not enforced by the Python interpreter, but they are a convention in Python.
#Protected attributes are used to indicate that the attribute should not be accessed from outside the class.

#The Consenting Adult Philosophy

#The Consenting Adult Philosophy is a principle in Python that states that developers should be allowed to access any part of the code, even if it is marked as private or protected.
#The Consenting Adult Philosophy is based on the idea that developers should be trusted to use the code responsibly and not abuse it.
#The Consenting Adult Philosophy is a way to promote a culture of trust and responsibility among developers.

