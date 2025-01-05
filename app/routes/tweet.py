from flask import g
from flask_restful import Resource
from marshmallow import Schema, fields, validate
from app.middlewares.auth import requires_auth
from app.middlewares.validation import validate_json
from app.models import Tweet as TweetModel
from sqlalchemy import desc


class TweetRequestSchema(Schema):
    message = fields.Str(required=True, validate=validate.Length(min=1, max=280))


class Tweet(Resource):
    def get(self):
        tweets = (
            g.session.query(TweetModel)
            .order_by(desc(TweetModel.created_at))
            .limit(10)
            .all()
        )

        return [
            {
                "id": tweet.id,
                "message": tweet.message,
                "user_name": tweet.user.name,
                "created_at": tweet.created_at.isoformat(),
                "updated_at": tweet.updated_at.isoformat(),
            }
            for tweet in tweets
        ]

    @requires_auth
    @validate_json(TweetRequestSchema())
    def post(self):
        tweet = TweetModel(user_id=g.user.id, message=g.json["message"])

        g.session.add(tweet)
        g.session.commit()

        return {
            "id": tweet.id,
            "message": "Tweet created successfully",
            "code": "TWEET_CREATED",
        }, 201
