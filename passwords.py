import secrets
import string

def name_of_global_obj(xx):
    return [objname for objname, oid in globals().items()
            if id(oid)==id(xx)][0]

class Password:
    passwords = {}
    # Initialization of password
    def __init__(self, style, size, name):
        self.name = name

        # generates new value and assigns it
        self.password = Password._generate(self, style, size)
        Password.passwords[name] = self.password 

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
        
        print(self)

   # Changing of password
    def _change(self, new_password = None, style = None, size = None):
        if new_password == None:
            self.password = Password._generate(self, style, size) 
        else:
            self.password = new_password
        Password.passwords[self.name] = self.password 
        

    # Deleting of password
    def _delete(name):
        del name
        del passwords[name]

class Interface():
    def __init__(self):
        self.string = str()
        print("\
\nHello, this is Gamayun!\nI'm password manager.\nType 'help' to see what I can\n")
        self._input()

    # Repeating cycle for taking commands from user
    def _input(self):
        while self.string != "exit":
            self.string = input("> ")
        
            if self.string == "help": # help tips
                print("\nThe options are:\
 \n\nhelp - to show this option\nnew - to create new password\
 \nlist - to list all passwords\nchange - to change password\
 \nremove - to delete password \n")

            elif self.string == "new": # creates new password
                self._new()

            elif self.string == "list": # lists passwords
                self._list()
            
            elif self.string == "change": # changes password
                self._change()

            elif self.string == "remove": # remove password
                self._delete()
            else:
                pass
    
    # Creating new password
    def _new(self):
        
        entered_password = {}
        name = input("\nEnter new password's name: ")
        size = int(input("Enter new password's length: "))
        style = input("Enter new password's style(mix, letters, numbers): ")
        print()

        while True:
            if style == "mix" or "letters" or "numbers":
                break
            else:
                style = input("Enter new password's style(mix, letters, numbers): ")

        # assignment of password
        entered_password[name] = entered_password.get(name, Password(style, size, name = name))
         
        dir({Password})
    # List of all the passwords
    def _list(self):
        print()
        [print(key,':',value) for key, value in Password.passwords.items()]
        print()

    # Changing of password
    def _change(self):
        entered_password = {}
        if Password.passwords: # handling passwords absence 
            self._list()
            name = input("Which one should be changed: ")

            while not (name in Password.passwords.keys()): # checking for presence
                name = input(f"There is no {name}. Enter again: ")
                
            do = input("Do you want gamayun to generate new password?(Y/n): ")

            if do == "Y":
                size = int(input("Enter new password's length: "))
                style = input("Enter new password's style(mix, letters, numbers): ")
                entered_password[name] = entered_password.get(name, Password(style, size, name = name))
                exec(f"{name}._change(None, style, size, name)") # temporary solution
            else:
                password = input("Enter new password: ")
                exec(f"{name}._change(password)")

        else: print("You have no passwords to change!")

# Main part of program
defined = Interface()
