from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "postgresql://postgres:6236@localhost:5432/myway"
    )

class BaseRepr():
    def __repr__(self):
        data = self.__dict__
        data = dict(filter(lambda x: x[0] not in '_sa_instance_state', data.items()))
        nl_char = '\n\t'
        out = list()
        for item, value in data.items():
            if item != list(data.keys())[-1]:
                if type(value) == int:
                    out.append(f"{item}: {value},")
                else:
                    out.append(f"{item}: '{value}',")
            else:
                if type(value) == int:
                    out.append(f"{item}: {value}")
                else:
                    out.append(f"{item}: '{value}'")

        return '{\n\t' + nl_char.join(out) + "\n}"

Base = declarative_base()

class User_profile(Base, BaseRepr):
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashpass = Column(String)
    salt = Column(String)
    name = Column(String)

class User_session(Base, BaseRepr):
    __tablename__ = 'user_session'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    session = Column(String)
    last_using = Column(DateTime)
