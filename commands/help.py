import os
from argparse import ArgumentParser

import manage
from root.base import BaseCommand


class Command(BaseCommand):
    help = 'Show this help message'

    def add_args(self, parser: ArgumentParser):
        pass

    def handle(self, *args, **kwargs):
        commands = os.listdir(os.path.dirname(__file__))
        print('[Commands]')
        for c in commands:
            if not c.endswith('.py'):
                continue

            command = c.replace('.py', '')
            method = manage.fetch(command)
            print('{:<10} \t {}'.format(command, method.help))
