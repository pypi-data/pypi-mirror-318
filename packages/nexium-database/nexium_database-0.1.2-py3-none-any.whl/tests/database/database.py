from nexium_database import Database
from tests.models.user import User


database = Database(
    url='mysql+aiomysql://root:PbsVsD7EGCXYe2E5pZC2rne8ZNZ0vfr@80.68.156.106:3306/yagroup_pay',
    models=[
        User,
    ],
)
