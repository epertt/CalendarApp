class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

    def __eq__(self, other):
        return self.username == other.username and self.password == other.password
