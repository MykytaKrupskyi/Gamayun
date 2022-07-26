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
        with open('data.json', 'w') as convert_file:
            convert_file.write(json.dumps(Passwords.passwords))

    # Reading of file
    #Passwords.passwords[name] = password 
    def _read():
        try:
            with open('data.json') as json_file:
                data = json.load(json_file)
                for index in range(0, len(data)-1):
                    names_list = list(data)
                    name = names_list[index]
                    Passwords.passwords[name] = data[name] 
        except: 
            print("NO data.json found!")
