from main import session
from models import User, Comment
# from sqlalchemy import select


# statement = select(User).where(User.username.in_(["Paul", "John"]))  # cause 1
# result = session.scalars(statement)
#
# for user in result:
#     print("User:", user)


users = session.query(User).all()

for user in users:
    print("User:", user)
