from models import User, Comment
from main import Session
from connect import engine


session = Session(bind=engine)

user1 = User(
    username="Jona",
    email_address="orm@gmail.com",
    comments=[Comment(text="Hello world"), Comment(text="Make sure")],
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

session.add_all([user1, paul, john])
session.commit()
