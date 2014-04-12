from abc import ABCMeta, abstractmethod

class PhoneBookLayerInterface(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass
    
    @abstractmethod
    def insert(self, record):
        """ 
        Insert a new phone book record,
        semicolon separated string:
        'name;address;phone_number'
        """
        pass

    @abstractmethod
    def lookup(self, name):
        """
        Search up phone book record by name.
        Returns semicolon separated string:
        'name;address;phone_number'
        If no entry, returns None
        """
        pass
