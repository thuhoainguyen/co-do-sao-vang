print("App Facebook ")
# yeu cau nguoi dung tao account(name, age, sex)
# yeu cau user add 3 friends
# user tao post xong hien post ra screen
# friends khac like vao post day
# hien ra bao nhieu nguoi like post day


class Account:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.friends= []
        self.posts = []

    def print_info_user(self, metadata = ""):
        print(f"This user is {self.name}, {self.age} years old, sex: {self.sex}")
        print("-----------")

    def add_friend(self, friend):
        self.friends.append(friend)
    
    def print_info_friend(self, metadata = ""):
        print(f"His friend is {self.name}, {self.age} years old, sex: {self.sex}")

    def show_friend(self):
        for i, friend in enumerate(self.friends):
            friend.print_info_friend(i+1)

    def create_post(self, ID, content):
        post = Post(ID, content)
        self.posts.append(post)

    def like_post(self, post):
        post.add_like()
    
    def print_posts(self):
        for post in self.posts:
            print(f"Post ID: {post.ID}\nPost content: {post.content}\nLikes: {post.likes}")

class Post:
    def __init__(self, ID, content):
        self.ID = ID
        self.content = content
        self.likes = 0
    
    def add_like(self):
        self.likes += 1


# ------------------------------------------
user = Account("Thu", 21, "F")
friend_1 = Account("Tung", 22, "M")
friend_2 = Account("Tu", 22, "M")
friend_3 = Account("Tam", 20, "F")

user.add_friend(friend_1)
user.add_friend(friend_2)
user.add_friend(friend_3)

user.print_info_user()
user.show_friend()

user.create_post(1023, "Toi la nguoi viet nam")

for post in user.posts:
    for friend in user.friends:
        print("-----------")
        status = str(input("Like the post? (Yes/No): "))
        if status == "Yes":
            friend.like_post(post)
print("-----------")
user.print_posts()