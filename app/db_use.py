from app.db_setup import User_profile, User_session

from uuid import uuid4
import datetime
import hashlib
import random
import string

# Функция хеширования
_hash = lambda x : hashlib.md5((x).encode()).hexdigest()

class DB_Activate():
    def __init__(self, session) -> None:
        self.session = session
    
    def db_decorator(func):
        def db_use(self, *args, **kwargs):
            result = None
            session = None

            try:
                session = self.session()
                result = func(*args, **kwargs, session=session)
            except Exception as err:
                print("ERR: ", err)
                if session is not None:
                    session.rollback()
            if session is not None:
                session.close()
            return result
        return db_use
    
    @db_decorator
    def get_first_filter(db_table, session=None, search=()):
        return session.query(db_table).filter(search).first()
    
    @db_decorator
    def get_all_filter(db_table, session=None, search=()):
        return session.query(db_table).filter(search).all()
    
    @db_decorator
    def add(db_table, session=None):
        session.add(db_table)
        session.commit()
        return db_table.id
    
    @db_decorator
    def update(db_table, reload={}, session=None, search=()):
        session.query(db_table).filter(search).update(reload)
        session.commit()
    
    @db_decorator
    def dell(db_table, session=None, search=()):
        db_list = session.query(db_table).filter(search).all()
        for db in db_list:
            session.delete(db)
        session.commit()

    @db_decorator
    def new_session(id, session=None):
        date_now = datetime.datetime.now(datetime.timezone.utc)
        user = User_session(user_id=id, last_using=date_now, session=(uuid4().hex))
        session.add(user)
        session.commit()

        return user.session
        
    @db_decorator
    def new_user(email, password, name, session=None):
        date_now = datetime.datetime.now(datetime.timezone.utc)
        _salt = ''.join(random.choice(string.ascii_letters) for x in range(30))
        _hashpass = _hash(password + _salt)

        db_user = User_profile(email=email, hashpass=_hashpass, salt=_salt, name=name)
        session.add(db_user)
        session.commit()

        db_user_session = User_session(user_id=db_user.id, last_using=date_now, session=(uuid4().hex))
        session.add(db_user_session)
        session.commit()

        return db_user_session.session