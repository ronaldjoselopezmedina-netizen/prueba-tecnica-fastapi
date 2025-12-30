from app.models.user import User
from app.core.security import hash_password

def create_initial_user(db):
    if not db.query(User).filter(User.username=="admin").first():
        user = User(username="admin", password_hash=hash_password("admin123"))
        db.add(user)
        db.commit()
