
from .phonebook_layer import PhoneBookLayer
from .version import __version__

class PhoneBookTerminal(object):
    def __init__(self):
        self.pbl = PhoneBookLayer()

    def start(self):
        self.output("")
        self.output("PHONE BOOK TERMINAL")
        self.output(__version__)
        while True:
            call = self.input("phonebook: ")
            splt = call.split(" ",1)
            command = splt[0]
            if command == "":
                continue
            elif command == "insert":
                try:
                    self.pbl.insert(splt[1])
                except:
                    self.print_missing()
            elif command == "lookup":
                try:
                    self.output(self.pbl.lookup(splt[1]))
                except:
                    self.print_missing()
            elif command == "help":
                self.print_help()
            elif command == "exit":
                self.output("have a nice day!")
                break
            else:
                self.print_unknown(command)

    # use a local handle for std input and output
    # to facilitate easy mocking
    input = raw_input

    def output(self,s):
        print s

    def print_missing(self):
        self.output(" Missing value or incorrect input syntax,")
        self.output(" type help for instructions")

    def print_unknown(self,cmd=""):
        self.output(" Unknown command '%s',"%cmd)
        self.output(" type help for instructions")

    def print_help(self):
        self.output(" ---------------------------------------")
        self.output(" PHONE BOOK TERMINAL INSTRUCTIONS")
        self.output(" ---------------------------------------")
        self.output("  insert <name>;<address>;<phone_number>")
        self.output("     inserts a new phonebook record")
        self.output("     into database.")
        self.output(" ")
        self.output("  lookup <name>")
        self.output("      fetch a record from database")
        self.output(" ")
        self.output("  help")
        self.output("      prints this help")
        self.output(" ")
        self.output("  exit")
        self.output("      exits the phone book terminal")
        self.output(" ---------------------------------------")
