class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # print(password)

    def check_password(self, password):
        return self.password == password
    
    @classmethod
    def get(cls, username):
        if username in cls.USERS:
            return cls(username)
        return None
    
    def is_authenticated(self):
        return True  # You can customize this based on your authentication logic

    def is_active(self):
        return True  # You can customize this based on your activation logic

    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.username)