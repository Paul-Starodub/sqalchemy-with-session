from main import session
from models import User


john = session.query(User).filter_by(username="John").first()
print(john)
