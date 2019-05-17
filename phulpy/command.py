import sys
import subprocess
from threading import Thread


class Command(object):
    def __init__(self, command, cwd, env, quiet, sync, on_stdout, on_stderr, on_finish):
        self.command = command
        self.cwd = cwd
        self.env = env
        self.quiet = quiet
        self.sync = sync
        self.on_stdout = on_stdout
        self.on_stderr = on_stderr
        self.on_finish = on_finish
        self.proc = None

        self.stdout = ''
        self.stderr = ''

    def enqueue_output(self, out, _type):
        for line in iter(out.readline, b''):
            if _type == 'out':
                if callable(self.on_stdout):
                    self.on_stdout(line.decode('ascii'))
                self.stdout = self.stdout + line.decode('ascii')
            else:
                if callable(self.on_stderr):
                    self.on_stderr(line.decode('ascii'))
                self.stderr = self.stderr + line.decode('ascii')

            if not self.quiet:
                stream = sys.stdout if _type == 'out' else sys.stderr
                stream.write(line.decode('ascii'))

        if self.proc.poll() is not None:
            if callable(self.on_finish):
                self.on_finish(self.proc.returncode, self.stdout, self.stderr)

    def start(self):
        command = self.command.split(' ')[0]
        args = self.command.split(' ')[1:]

        ON_POSIX = 'posix' in sys.builtin_module_names
        self.proc = subprocess.Popen(
            [command] + args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
            close_fds=ON_POSIX,
            env=self.env,
            cwd=self.cwd
        )

        thread1 = Thread(
            target=self.enqueue_output,
            args=(self.proc.stdout, 'out')
        )
        thread1.daemon = False
        thread1.start()

        thread2 = Thread(
            target=self.enqueue_output,
            args=(self.proc.stderr, 'err')
        )
        thread2.daemon = False
        thread2.start()

        if self.sync:
            thread1.join()
            thread2.join()

            self.proc.wait()
            self.exit_code = self.proc.returncode
