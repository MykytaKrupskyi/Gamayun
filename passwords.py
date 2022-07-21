import secrets
import string

class Password:
    def __init__(self, style, size):

        self.style= style
        self.size = size

        # decision-making statement for password type
        if self.style == "letters":
            sample = string.ascii_letters 
        elif self.style == "numbers":
            sample = string.string.digits
        else:
            sample = string.ascii_letters + string.digits

        # the generating line itself
        password = ''.join(secrets.choice(sample) for i in range(self.size))
        self.password = password

class Interface():
    def __init__(self):
        self.string = str()
        d = {} # saves the password names 

        print("""Hello, this is Gamayun!
I'm password manager.
Type 'help' to see what I can""")

        while self.string != "exit":
            self.string = input(">")
        
            # Help menu
            if self.string == "help":
                print("""The options are:
help - to show this option
new - to create new password """)

        # Creating new password
            elif self.string == "new":
                name = input("Enter new password's name: ")
                length = int(input("Enter new password's length: "))
                style = input("Enter new password's style(mix, letters, numbers): ")
                
                while True:
                    if style == "mix" or "letters" or "numbers":
                        break
                    else:
                        style = input("Enter new password's style(mix, letters, numbers): ")

                exec("{0} = Password(style, length)".format(name)) # temporary solution!!!

            else:
                pass

defined = Interface()
