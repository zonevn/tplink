from root.base import BaseCommand
from argparse import ArgumentParser

from root.iostream import get_pickle


class Command(BaseCommand):
    help = 'Show the Router\'s current profile. All information is read-only.'

    def add_args(self, parser: ArgumentParser):
        pass

    def handle(self, *args, **kwargs):
        persists = get_pickle('db.pickle')
        print("Host: {0}".format(persists.get('host')))
        print("Account: {0}".format(persists.get('account')))
