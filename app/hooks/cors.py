from flask import request


def register_cors_hook(app):

    @app.after_request
    def after_request(response):
        # https://stackoverflow.com/a/52875875/1217998
        allowed_origins = [
            "http://localhost:3000",
            "https://app.cluster.ad-absurdum.me",
        ]

        # Get the request origin
        origin = request.headers.get("Origin")

        # If the origin is in our allowed list, set it in the response
        if origin in allowed_origins:
            response.headers.add("Access-Control-Allow-Origin", origin)
            response.headers.add(
                "Access-Control-Allow-Headers", "content-type, set-cookie"
            )
            response.headers.add("Access-Control-Allow-Methods", "*")
            response.headers.add("Access-Control-Allow-Credentials", "true")

        return response
