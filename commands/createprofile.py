from argparse import ArgumentParser

from root.base import BaseCommand
from root.iostream import put_pickle


class Command(BaseCommand):
    help = 'Create a PPPoE connection profile, only at first if not change.'

    def add_args(self, parser: ArgumentParser):
        pass

    def handle(self, *args, **kwargs):
        host = input("Host: ")
        acc = input("Account: ")
        pwd = input("Password: ")
        put_pickle('db.pickle', {'host': host, 'account': acc, 'password': pwd})
