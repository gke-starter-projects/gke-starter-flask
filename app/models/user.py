import datetime
import jwt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text
from marshmallow import Schema, fields
from app.models.base import Base
from app.config import Config
from sqlalchemy.orm import relationship


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    name = fields.Str()
    password = fields.Str()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(Text, unique=True)
    name = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    tweets = relationship("Tweet", back_populates="user")

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def dump(self):
        return UserSchema().dump(self)

    def generate_token(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        payload = {
            "exp": now + datetime.timedelta(minutes=15),
            "iat": now,
            "sub": str(self.id),
        }

        return jwt.encode(
            payload,
            Config.JWT_SECRET,
            algorithm=Config.JWT_ALGORITHM,
        )
