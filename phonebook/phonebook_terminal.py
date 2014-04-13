"""
This module impelements an interactive terminal
for insert and lookup of phone book entries in
a database.
"""

from .dummydb_phonebook_layer import DummydbPhoneBookLayer
from .version import __version__

class PhoneBookTerminal(object):
    """
    An interactive terminal for insert and lookup of
    phonebook entries in a database.
    """
    def __init__(self):
        self.pbl = DummydbPhoneBookLayer()

    def start(self):
        """
        Starts the terminal session.
        """
        self.output("")
        self.output("PHONE BOOK TERMINAL")
        self.output(__version__)
        while True:
            call = self.input("phonebook: ")
            splt = call.split(" ", 1)
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
    # -- facilitates easy mocking
    input = raw_input

    def output(self, string):
        """
        Local std output handle.
        Allows for easy mocking during unit testing.
        """
        print string

    def print_missing(self):
        """
        Report missing or incorrect input syntax.
        """
        self.output(" Missing value or incorrect input syntax,")
        self.output(" type help for instructions")

    def print_unknown(self, cmd=""):
        """
        Report an unknown command
        """
        self.output(" Unknown command '%s',"%cmd)
        self.output(" type help for instructions")

    def print_help(self):
        """
        Print out documentation.
        """
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
