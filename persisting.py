from models import User, Comment


user1 = User(
    username="Jona",
    email_address="orm@gmail.com",
    comments=[Comment(text="Hello world"), Comment(ttext="Make sure")],
)


paul = User(
    username="Paul",
    email_address="polst@gmail.com",
    comments=[Comment(text="Hello dear"), Comment(text="Done")],
)

john = User(
    username="John",
    email_address="777@gmail.com",
)
