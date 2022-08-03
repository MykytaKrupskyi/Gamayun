import string
import secrets
import json
from cryptography.fernet import Fernet
import os

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
            with open("saved.json", "w") as outfile: #writes dict
                json.dump(Passwords.passwords, outfile)

            if os.path.isfile('filekey.key'): #reads key
                with open('filekey.key', 'rb') as filekey:
                    key = filekey.read()

            else: #generates key
                key = Fernet.generate_key()
                with open('filekey.key', 'wb') as filekey:
                   filekey.write(key)

            fernet = Fernet(key)

            # Encryptes file
            with open('saved.json', 'rb') as file:
                original = file.read()

            encrypted = fernet.encrypt(original)

            with open('saved.json', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
    
    # Reading of file
    def _read():
        try:
            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()
            fernet = Fernet(key) 

            with open('saved.json', 'rb') as enc_file:
                encrypted = enc_file.read()

            decrypted = fernet.decrypt(encrypted)
            saved = decrypted.decode("utf-8") 

            Passwords.passwords = json.loads(saved)

        except:
            print("no savings")
