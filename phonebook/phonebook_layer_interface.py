"""
Module that defines an interface to
a database for phone book entries.
"""

from abc import ABCMeta, abstractmethod

class PhoneBookLayerInterface(object):
    """
    Defining an interface for the phone book database layer
    """

    __metaclass__ = ABCMeta
    
    @abstractmethod
    def insert(self, record):
        """ 
        Insert a new phone book record,
        semicolon separated string:
        'name;address;phone_number'
	Any leading or trailing spaces will be stipped.
        """
        pass

    @abstractmethod
    def lookup(self, name):
        """
        Search up phone book record by name.
        Returns semicolon separated string:
        'name;address;phone_number'
        If no entry, returns None
	Any leading or trailing spaces will be stipped.
        """
        pass
