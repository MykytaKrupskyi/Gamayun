import string
import secrets
import json

class Passwords:
    passwords = {}

    # Creation of new password
    def _new(name, size, style):
        password = Passwords._generate(size, style)
        Passwords.passwords[name] = password 

    # Generation of password
    def _generate(size, style):
        # listing possible symbols
        sample = ""
        if style[0] == True:
            sample += string.ascii_lowercase 
        else: pass
        if style[1] == True:
            sample += string.ascii_uppercase
        else: pass
        if style[2] == True:
            sample += string.digits
        else: pass
        if style[3] == True:
            sample += "+-_*%#@"
                
        # the generating line itself
        password = ''.join(secrets.choice(sample) for i in range(size))

        return password

    # Changing of password manually
    def _change_manualy(name, entered_password):
        password = entered_password 
        Passwords.passwords[name] = password 

    # Changing of password with generation
    def _change_auto(name, size, style):
        password = Passwords._generate(size, style)
        Passwords.passwords[name] = password 

    # Deleting of password
    def _delete(name):
        del Passwords.passwords[name]

    # Writing to file
    def _write():
        with open('details.json', 'w') as convert_file:
            convert_file.write(json.dumps(Passwords.passwords))

    
