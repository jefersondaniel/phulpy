Phulpy
======

The task manager for python

Why
~~~

Port of GulpJS for Python

Documentation
~~~~~~~~~~~~~

Usage
^^^^^

Install:
''''''''

.. code:: bash

   $ pip install phulpy

Create your ``phulpyfile.py`` (the configuration file, that describes all your tasks):
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

   from phulpy import task


   @task
   def default():
       print("Hello world")


   @task
   def mytask():
       print("You called my task")

Run:
''''

Run the phulpy over the ``phulpyfile.py`` directory

.. code:: bash

   $ phulpy --help
   $ phulpy # Will run the `default` task
   $ phulpy mytask # Will run the `mytask` task
