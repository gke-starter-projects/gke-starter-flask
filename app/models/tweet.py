import datetime
from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from app.models.base import Base
from app.config import Config


class TweetSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    message = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class Tweet(Base):
    __tablename__ = "tweet"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(
        DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    updated_at = Column(
        DateTime,
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
        onupdate=lambda: datetime.datetime.now(datetime.timezone.utc),
    )

    # Relationship to User model
    user = relationship("User", back_populates="tweets")


def dump_tweet(tweet):
    return TweetSchema().dump(tweet)
