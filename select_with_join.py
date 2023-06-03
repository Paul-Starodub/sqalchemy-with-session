from main import session
from models import User, Comment
from sqlalchemy import select


statement = (
    select(Comment)
    .join(Comment.user)
    .where(User.username == "Paul")
    .where(Comment.text == "Make sure")
)

result = session.scalars(statement)

print(result)
