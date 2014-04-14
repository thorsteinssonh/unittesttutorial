==========================
Unittest tutorial 
==========================
--------------------------------
practical exercise
--------------------------------

:Date: 12-04-2014
:Version: 0.1
:Authors: - Hrobjartur Thorsteinsson 
          - (thorsteinssonh@gmail.com)

Assignment
==========================
Your assignment is to implement a missing
unittest for the **phonebook** package.

This exercise is also intented to
demonstrate how you can use some
common python tools to test and
evaluate your python projects.

Install software tools
====================================
The essential tools are,

.. code:: bash

	$ sudo apt-get install python-mock
	$ sudo apt-get install python-nose

Optionally, if you want to compile
UML diagrams or documentation,

.. code:: bash

	$ sudo apt-get install graphviz
	$ sudo apt-get install pylint
	$ sudo apt-get install python-coverage
	$ sudo apt-get install rst2pdf

**rst2pdf** depends on docutils, which should therefore also be installed.
With docutils you get more tools, such as **rst2html**.

run the tests
++++++++++++++++++++++++++

The **nose** package includes a 'testrunner' called
**nosetests**.  The testrunner automatically looks up
classes that derive from unittest.TestCase
executes the tests and reports a result.

Run,

.. code:: bash

	$ nosetests -v tests/

to execute all the tests found in the tests directory.
The following two tests have been defined but not
implemented,

ERROR: test_lookup (test_dummydb_phonebook_layer.TestPhoneBookLayer)
ERROR: test_terminal_unknown_command (test_phonebook_terminal.TestPhoneBookTerminal)
	
We are going to implement the **TestPhoneBookLayer.test_lookup** inside
the file **tests/test_dummydb_phonebook_layer.py**

phonebook structure
++++++++++++++++++++++++++

.. code:: bash

	$ pyreverse -o png phonebook/*.py

.. image:: class_diagram.png
	:width: 700px 


