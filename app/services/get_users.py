from app.db.models.users import User
from sqlalchemy import select

def get_all_user(session):
    stmt = select(User)
    result = session.execute(stmt)
    return result.scalars().all()