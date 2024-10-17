# entity/user.py

class User:
    def __init__(self, userId: int, username: str, password: str, role: str):
        self.__userId = userId
        self.__username = username
        self.__password = password
        self.__role = role

    # Getters and Setters
    @property
    def userId(self):
        return self.__userId

    @userId.setter
    def userId(self, value):
        self.__userId = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    # toString equivalent
    def __str__(self):
        return f"User[ID={self.__userId}, Username={self.__username}, Role={self.__role}]"
