import unittest
from mock import Mock

from phonebook import PhoneBookLayer

class TestPhoneBookLayer(unittest.TestCase):
    def setUp(self):
        self.pbl = PhoneBookLayer()
        self.pbl.db.add = Mock()
        
    def test_insert(self):
        self.pbl.insert("Vedurstofan;Bustadavegi 7;5226000")
        self.pbl.db.add.assert_called_with('phone_book',
                                           'Vedurstofan',
                                           'Bustadavegi 7',
                                           5226000)

    def test_lookup(self):
        raise NotImplementedError("Implement this test please!")
