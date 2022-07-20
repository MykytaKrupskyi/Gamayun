import secrets
import string

class Password:
    def __init__(self, typee, size):

        self.type = typee
        self.size = size

        # decision-making statement for password type
        if self.type == "letters":
            sample = string.ascii_letters 
            
        elif self.type == "numbers":
            sample = string.string.digits

        elif self.type == "mix":
            sample = string.ascii_letters + string.digits
        
        else:
            sample = 0

        # the generating line itself
        password = ''.join(secrets.choice(sample) for i in range(self.size))
        self.password = password

# test
google = Password("mix", 12)
print("Password generated for google is {0}".format(google.password))
