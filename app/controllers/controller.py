from flask import Flask, jsonify

from app.components.component import UserComponent

app = Flask(__name__)
user_component = UserComponent()


@app.route("/api/users", methods=["GET"])
def get_user():
    """REST API endpoint to fetch user details."""
    try:
        user_data = user_component.get_all_users()
        return jsonify(user_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
