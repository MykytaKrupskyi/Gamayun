import string
import secrets

class Passwords:
    passwords = {}

    # Creation of new password
    def _new(style, size, name):
        password = Passwords._generate(style, size)
        Passwords.passwords[name] = password 

    # Generation of password
    def _generate(style, size):
        # decision of password type
        if style == "letters":
            sample = string.ascii_letters 
        elif style == "numbers":
            sample = string.digits
        elif style == "mix":
            sample = string.ascii_letters + string.digits

        # the generating line itself
        password = ''.join(secrets.choice(sample) for i in range(size))
        return password

    # Changing of password manually
    def _change_manualy(name, entered_password):
        password = entered_password 
        Passwords.passwords[name] = password 

    # Changing of password with generation
    def _change_auto(name, style, size):
        password = Passwords._generate(style, size)
        Passwords.passwords[name] = password 

    # Deleting of password
    def _delete(name):
        del Passwords.passwords[name]


