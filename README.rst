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

   from phulpy import task, Output


   @task
   def default(phulpy):
       phulpy.start(['mytask'])


   @task
   def mytask(phulpy):
       Output.out(
           Output.colorize("You called my task", "green")
       )

Run:
''''

Run the phulpy over the ``phulpyfile.py`` directory

.. code:: bash

   $ phulpy --help
   $ phulpy # Will run the `default` task
   $ phulpy mytask # Will run the `mytask` task
