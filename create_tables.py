from app.database import engine
from app.models.user import User
from app.models.task import Task

User.metadata.create_all(bind=engine)
Task.metadata.create_all(bind=engine)

print("Tablas creadas")
