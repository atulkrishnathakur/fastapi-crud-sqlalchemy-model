from app.db.models.users import User
from sqlalchemy import select

def update_user_by_id(session, userdata):
    stmt = select(User).where(User.id == userdata['id'])
    result = session.execute(stmt)
    dbuser = result.scalars().first()

    dbuser.name = userdata['name']
    dbuser.email = userdata['email']
    session.add(dbuser)
    session.commit()
    session.refresh(dbuser)
    return dbuser