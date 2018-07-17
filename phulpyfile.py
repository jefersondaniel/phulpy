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
