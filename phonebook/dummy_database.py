"""
A module implementing a very simple
'dummy' database, simulating a typical
database functionality
"""

class DummyDataBase(object):
    """
    Dummy database for simulating
    typical database functionality
    """
    # first key is the unique key
    table_defs = {'phone_book':('name', 'address', 'phone_number')}

    # table data is a dict, "unique key":(data1,data2,...)
    data = {'phone_book':{}}

    def add(self, table_name, *args):
        """
        Add entry into a database table.
        Accepts unlimited number of arguments representing
        column entries in the table.
        """
        # get table definition
        keys = self.table_defs[table_name]

        # check input of same length as keys
        if len(args) != len(keys):
            raise ValueError("Number of database table keys do not match input")

        # get the table data holder
        table = self.data[table_name]

        # add / replace the data
        table[args[0]] = args[1:]
        
    def get(self, table_name, unique_key):
        """
        Search for entry in database from a unique_key value.
        If entry exists, returns a tuble of remaining values,
        else returns None.
        """
        # get the table data holder
        table = self.data[table_name]
        # return the data or None
        try:
            return table[unique_key]
        except KeyError:
            return None
