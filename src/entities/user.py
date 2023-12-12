class User:
    """Class representing a user
    
        Attributes:
            user_id: an integer representing user who is being represented
            username: a string representing the user's username
            password: a string representing the user's password
    """
    def __init__(self, username, password, user_id=None):
        self.user_id = user_id
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

    def __eq__(self, other):
        return (self.user_id == other.user_id
                and self.username == other.username
                and self.password == other.password)
