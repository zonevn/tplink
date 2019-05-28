from root.base import BaseCommand
from argparse import ArgumentParser

from root.iostream import get_pickle


class Command(BaseCommand):
    help = 'Show the Router\'s current profile. All information is read-only.'

    def add_args(self, parser: ArgumentParser):
        pass

    def handle(self, *args, **kwargs):
        persists = get_pickle('db.pickle')
        assert persists.get('account'), "You must to create a profile at first."

        print("Host: {}".format(persists.get('host')))
        print("Account: {}".format(persists.get('account')))
        print("Password: {}".format(persists.get('password')))
