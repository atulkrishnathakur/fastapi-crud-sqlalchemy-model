from app.db.models.users import User
from app.utils.hashing import Hash

def create_new_user(session, userdata):
    hashed_pwd = Hash.create_hash(userdata['password'])
    user = User(
        name=userdata['name'],
        email=userdata['email'],
        password=hashed_pwd
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
