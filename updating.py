from main import session
from models import User, Comment


comment = session.query(Comment).filter_by(id=1).first()

comment.text = "New text"
session.commit()
