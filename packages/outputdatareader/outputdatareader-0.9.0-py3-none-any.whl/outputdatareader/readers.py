class Base():
    def __init__(self, scanner, holder):
        self.scanner = scanner
        self.holder = holder

    def read(self):
        try:
            self.setup()
            try:
                for line in self.scanner:
                    try:
                        self.loop(line)
                    except ContinueToNextLoop:
                        pass
            except ExitLoop:
                pass
            self.teardown()
        except ExitRead:
            pass
        return self.holder

    def result(self):
        return self.holder

    # Override following methods: 'setup', 'loop' and 'teardown'.
    # At least, you must override 'loop' method.

    def setup(self):
        pass

    def loop(self, line):
        pass

    def teardown(self):
        pass

    # private methods.

    def _exit_loop(self):
        raise ExitLoop()

    def _exit_read(self):
        raise ExitRead()

    def _next_loop(self):
        raise ContinueToNextLoop()

    def _unshift(self):
        self.scanner.unshift()


class ReaderException(Exception):
    pass

class ExitLoop(ReaderException):
    pass

class ExitRead(ReaderException):
    pass

class ContinueToNextLoop(ReaderException):
    pass
