from app.services.service import UserService


class UserComponent:
    def __init__(self):
        self.client = UserService()

    def get_all_users(self):
        """Fetch and process user data."""
        user_data = self.client.get_all_users()
        # Add any additional processing logic here
        return user_data
