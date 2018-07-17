Phulpy
======

|Build Status| |Version|

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
       def print_file(file):
           Output.out(Output.colorize(
               file.relative_path,
               'green'
           ))

       def print_src_class(src):
           Output.out(src.__class__.__name__)

       def if_phulpy_file(file):
           return 'phulpyfile.py' in file.name

       phulpy.src(['./*'], read=True) \
           .pipe(phulpy.iterate(print_file)) \
           .pipe(print_src_class) \
           .pipe(phulpy.filter(if_phulpy_file)) \
           .pipe(phulpy.iterate(print_file)) \
           .pipe(phulpy.dest('./var'))


   @task
   def clean(phulpy):
       phulpy.src(['./var/*']) \
           .pipe(phulpy.clean())


   @task
   def do_nothing():
       pass

Run:
''''

Run the phulpy over the ``phulpyfile.py`` directory

.. code:: bash

   $ phulpy --help
   $ phulpy # Will run the `default` task
   $ phulpy mytask # Will run the `mytask` task
   $ phulpy --threads 4 mytask1 mytask2  # Will run the tasks simultaneously

By:
''''
@jefersondaniel
@reisraff


.. |Build Status| image:: https://travis-ci.org/jefersondaniel/phulpy.svg
   :target: https://travis-ci.org/jefersondaniel/phulpy

.. |Version| image:: https://badge.fury.io/py/phulpy.svg
   :target: https://pypi.python.org/pypi/phulpy
