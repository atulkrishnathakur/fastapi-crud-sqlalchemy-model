from app.db.models.users import User
from sqlalchemy import select

def delete_user_by_id(session, userdata):
    stmt = select(User).where(User.id == userdata['id'])
    result = session.execute(stmt)
    dbuser = result.scalars().first()
    session.delete(dbuser)
    session.commit()
    return "user deleted"