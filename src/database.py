from passwords import *

from cryptography.fernet import Fernet
import os
import json

class database:
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
