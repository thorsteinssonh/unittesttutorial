import unittest
from mock import Mock, patch

from phonebook import PhoneBookTerminal


class TestPhoneBookTerminal(unittest.TestCase):

    def setUp(self):
        self.terminal = PhoneBookTerminal()
        self.terminal.output = Mock()
        self.terminal.pbl.insert = Mock()
        self.terminal.pbl.lookup = Mock(return_value="Siggi;Krummaholum;12345")

    def test_insert(self):
        # make terminal called with insert ... followed by exit
        self.terminal.input = Mock(side_effect=["insert john;home;123",
                                                "exit"])
        # run the terminal
        self.terminal.start()
        # assert database insert
        self.terminal.pbl.insert.assert_called_with('john;home;123')

    def test_goodbye_message(self):
        # make terminal exit immediately
        self.terminal.input = Mock(return_value="exit")
        # run the terminal
        self.terminal.start()
        # assert goodbye message
        self.terminal.output.assert_called_with('have a nice day!')

    def test_lookup(self):
        # make terminal called with lookup ... followed by exit
        self.terminal.input = Mock(side_effect=["lookup Siggi",
                                                "exit"])
        # run the terminal
        self.terminal.start()
        # assert record output
        self.terminal.output.assert_any_call('Siggi;Krummaholum;12345')

    def test_unknown_command(self):
        raise NotImplementedError("Next implement this test, only if you have time")
