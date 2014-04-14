"""
Module implementing a PhoneBoookLayer
interface for the Dummy Database.
"""

from .dummy_database import DummyDataBase
from .phonebook_layer_interface import PhoneBookLayerInterface

class DummydbPhoneBookLayer(object):
    """
    PhoneBookLayer connecting to the
    Dummy Database class
    """
    __implements__ = (PhoneBookLayerInterface,)

    db = DummyDataBase()

    def insert(self, record):
        """ 
        Insert a new phone book record,
        semicolon separated string:
        'name;address;phone_number'
        Any leading or trailing spaces will be stripped.
        """
        name, address, phone_number = record.split(';')
        name = name.strip()
        address = address.strip()
        self.db.add('phone_book', name, address, int(phone_number))

    def lookup(self, name):
        """
        Search up phone book record by name.
        Returns semicolon separated string:
        'name;address;phone_number'
        If no entry, returns None
        Any leading or trailing spaces will be stripped.
        """
        name = name.strip()
        record = self.db.get('phone_book', name)
        if record is None:
            return None
        else:
            return name+";"+record[0]+";"+str(record[1])
