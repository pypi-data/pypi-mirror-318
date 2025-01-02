from nexium_database import BaseRepository
from tests.models.user import User


class UserRepository(BaseRepository[User]):
    def __init__(self, session):
        super().__init__(User, session=session)
