import secrets
import string

class Password:
    passwords = {}
    # Initialization of password
    def __init__(self, style, size, name=None):
        self.name = name

        # generates new value and assigns it
        self.password = Password._generate(self, style, size)
        Password.passwords[name] = self.password 

    # Changing of password
    def _change(self, style, size):
        self.password = new

    # Generation of password
    def _generate(self, style, size):
        self.style= style
        self.size = size

        # decision-making statement for password type
        if self.style == "letters":
            sample = string.ascii_letters 
        elif self.style == "numbers":
            sample = string.digits
        elif self.style == "mix":
            sample = string.ascii_letters + string.digits

        # the generating line itself
        password = ''.join(secrets.choice(sample) for i in range(self.size))
        return password

class Interface():
    def __init__(self):
        self.string = str()
        print("\nHello, this is Gamayun!\nI'm password manager.\nType 'help' to see what I can\n")
        self._input()

    # Repeating cycle for taking commands from user
    def _input(self):
        while self.string != "exit":
            self.string = input("> ")
        
            if self.string == "help": # help tips
                print("\nThe options are:\n\nhelp - to show this option\nnew - to create new password\nlist - to list all passwords\nchange - to change password\nremove - to delete password \n")

            elif self.string == "new": # creates new password
                self._new()

            elif self.string == "list": # lists passwords
                self._list()
            
            elif self.string == "change": # changes password
                self._change()

            else:
                pass
    
    # Creating new password
    def _new(self):

        name = input("\nEnter new password's name: ")
        length = int(input("Enter new password's length: "))
        style = input("Enter new password's style(mix, letters, numbers): ")
        print()

        while True:
            if style == "mix" or "letters" or "numbers":
                break
            else:
                style = input("Enter new password's style(mix, letters, numbers): ")
        
        locals()[name] = Password(style, length, name)

    # Lists all the passwords
    def _list(self):
        print()
        [print(key,':',value) for key, value in Password.passwords.items()]
        print()

defined = Interface()
