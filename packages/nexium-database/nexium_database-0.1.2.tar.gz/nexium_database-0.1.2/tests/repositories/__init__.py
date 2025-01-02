from tests.database.database import database
from tests.repositories.user import UserRepository


user_repo = UserRepository(session=database.session)
