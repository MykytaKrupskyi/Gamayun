import secrets
import string

class Password:
    passwords = {}
    def __init__(self, style, size, name=None):
        
        # assignment of variables
        self.style= style
        self.size = size
        self.name = name

        # decision-making statement for password type
        if self.style == "letters":
            sample = string.ascii_letters 
        elif self.style == "numbers":
            sample = string.digits
        else:
            sample = string.ascii_letters + string.digits

        # the generating line itself
        password = ''.join(secrets.choice(sample) for i in range(self.size))
        self.password = password

        # adding values to dictionary
        Password.passwords[name] = password 

class Interface():
    def __init__(self):
        self.string = str()

        print("Hello, this is Gamayun!\nI'm password manager.\nType 'help' to see what I can")

        # Repeating cycle for taking commands from user
        while self.string != "exit":
            self.string = input("> ")
        
            # Help menu
            if self.string == "help":
                print("""The options are:\nhelp - to show this option\nnew - to create new password\nlist - to list all passwords""")

            # Creating new password
            elif self.string == "new":
                self._new()

            # Listing all passwords
            elif self.string == "list":
                self._list()

            else:
                pass

    def _new(self):

        name = input("Enter new password's name: ")
        length = int(input("Enter new password's length: "))
        style = input("Enter new password's style(mix, letters, numbers): ")
        
        while True:
            if style == "mix" or "letters" or "numbers":
                break
            else:
                style = input("Enter new password's style(mix, letters, numbers): ")
        
        locals()[name] = Password(style, length, name)  

    def _list(self):
        [print(key,':',value) for key, value in Password.passwords.items()]

defined = Interface()
