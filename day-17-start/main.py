class User: # class names should be PascalCase
    pass # temp value to keep something empty for now

    # constructor
    def __init__(self, username, user_id):
        # initilization attributes
        self.username = username
        self.id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# inefficient way
# user_1.id = "001"
# user_1.username = "Anko"


# better way
user_1 = User(username="mike", user_id="001")
user_2 = User(username="pete", user_id="002")


print(user_1.username)
print(user_2.followers)

user_2.follow(user_1)
print(f"User 1 followers: {user_1.followers} and following {user_1.following}")
print(f"User 2 followers: {user_2.followers} and following {user_2.following}")