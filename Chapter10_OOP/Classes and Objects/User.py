class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def say_hi_to_user(self,user):
        print(f'Hello {user.username}, my name is {self.username}.')

user1 = User('ranit','ranit0120@gmail.com','123456')
user2 = User('john','john@example.com','password')

user1.say_hi_to_user(user2)