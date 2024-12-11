# userSession.py
class UserSession:
    current_user = None

    @staticmethod
    def set_current_user(username):
        UserSession.current_user = username

    @staticmethod
    def get_current_user():
        return UserSession.current_user