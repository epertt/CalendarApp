class Config:
    """A class representing a user's configuration
    
        Attributes:
            user_id: an integer representing user whose config is being represented
            settings: a dictionary representing individual config setting values
    """
    def __init__(self, user_id, settings=None):

        self.user_id = user_id
        self.settings = settings
