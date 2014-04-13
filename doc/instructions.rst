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

This tutorial also shows you how you can use some
common python tools to help you evaluate
and view python code projects.

phonebook structure
++++++++++++++++++++++++++

.. code:: bash

	$ pyreverse -o png phonebook/*.py

.. image:: class_diagram.png
	:width: 500px 

Install following software tools
====================================
The tools

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


Using nosetests and coverage
====================================

The **nose** package includes a commandline tool
**nosetests**.  This is perhaps the most popular
"testrunner" in python. This test runner automatically looks up
classes that derive from unittest.TestCase, sets some
environment conditions and executes the tests.

Run,

.. code:: bash

	$ nosetests -v tests/

to run the tests

