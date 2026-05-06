from app.db.models.users import User

def create_new_user(session, userdata):
    user = User(
        name=userdata['name'],
        email=userdata['email'],
        password=userdata['password']
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
