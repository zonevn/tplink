import argparse
import os


class BaseCommand:
    help = ''

    def create_parser(self, prog_name, command):
        parser = argparse.ArgumentParser(
            prog='%s %s' % (os.path.basename(prog_name), command),
            description=self.help or None,
        )

        self.add_args(parser)
        return parser

    def add_args(self, parser):
        pass

    def run(self, argv):
        parser = self.create_parser(argv[0], argv[1])
        options = parser.parse_args(argv[2:])
        kwargs = vars(options)
        args = kwargs.pop('args', ())
        self.handle(*args, **kwargs)

    def handle(self, *args, **kwargs):
        raise NotImplementedError('subclasses of BaseCommand must provide a handle() method')
