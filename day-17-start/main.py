class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def __str__(self):
        return f"{self.id} Nombre: {self.username}, followers {self.followers} , siguiendo {self.following}"


user_1 = User("0001", "David")
user_2 = User("0002", "Edna")
user_3 = User("0003", "Tenoch")

user_3.follow(user_1)
user_2.follow(user_1)
user_1.follow(user_3)
print(user_1)
