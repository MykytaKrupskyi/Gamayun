import string
import secrets
import json
from cryptography.fernet import Fernet

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
        try:
            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()
        except:
            key = Fernet.generate_key()
            with open('filekey.key', 'wb') as filekey:
                filekey.write(key)

        fernet = Fernet(key)
        passwords_data = str(Passwords.passwords).encode()
        encrypted_passwords_data = str(fernet.encrypt(passwords_data))
        with open('saved.json', 'w') as convert_file:
            convert_file.write(encrypted_passwords_data)

    # Reading of file
    def _read():
        try:
            with open('saved.json') as json_file:
                data = json.load(json_file)
                for index in range(0, len(data)-1):
                    names_list = list(data)
                    name = names_list[index]
                    Passwords.passwords[name] = data[name] 
        except: 
            print("NO saved.json found!")
