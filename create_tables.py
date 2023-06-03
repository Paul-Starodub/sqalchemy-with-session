from models import Base, User, Comment
from connect import engine


Base.metadata.create_all(bind=engine)
