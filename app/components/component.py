from app.services.service import UserService


class UserComponent:
    def __init__(self):
        self.client = UserService()

    def get_all_users(self):
        user_data = self.client.get_all_users()
        return user_data
