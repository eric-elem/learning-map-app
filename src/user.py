class User:
    # Initializes a user with the name attribute passed
    def __init__(self, name):
        self.name =name
    
    # Returns the name of a user
    def get_name(self):
        return self.name