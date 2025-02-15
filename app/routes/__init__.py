from app.routes.health import Health
from app.routes.user import User
from app.routes.login import Login
from app.routes.signup import Signup
from app.routes.tweet import Tweet


def register_routes(api):
    api.add_resource(Health, "/health", endpoint="health")
    api.add_resource(Health, "/", endpoint="root_health")
    api.add_resource(User, "/user/<int:user_id>", "/user")
    api.add_resource(Signup, "/signup")
    api.add_resource(Login, "/login")
    api.add_resource(Tweet, "/tweet")
