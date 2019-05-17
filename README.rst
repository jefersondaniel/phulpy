Phulpy
======

|Build Status| |Version| |Pyversions|

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
    def exec_1(phulpy):
        def __on_stdout__(tick, stdin):
            # Output.out(tick)

            if '[yes]?' in tick:
                stdin.write('yes\n')

        def __on_stderr__(tick, stdin):
            # Output.err(tick)
            pass

        def __on_finish__(sigint, stdout, stderr):
            pass

        phulpy.exec(
            'ls -lah',
            quite=False,  # write on stdout and stdin, default True, needs to be handled
            sync=False,  # default True
            on_stdout=__on_stdout__,  # handle stdout
            on_stderr=__on_stderr__,  # handle stderr
            on_finish=__on_finish__  # handle sigint
        )


    @task
    def exec_2(phulpy):
        # when its is sync return a command with stdout, stderr, and sigint
        command = phulpy.exec('ls -lah')

        sigint = command.sigint
        stdout = command.stdout
        stderr = command.stderr

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


`@jefersondaniel <https://github.com/jefersondaniel>`


`@reisraff <https://github.com/reisraff>`

.. |Build Status| image:: https://travis-ci.org/jefersondaniel/phulpy.svg
   :target: https://travis-ci.org/jefersondaniel/phulpy

.. |Version| image:: https://badge.fury.io/py/phulpy.svg
   :target: https://pypi.python.org/pypi/phulpy

.. |Pyversions| image:: https://img.shields.io/pypi/pyversions/phulpy.svg
   :target: https://pypi.python.org/pypi/phulpy
