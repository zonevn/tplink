from argparse import ArgumentParser

from includes.tplink import WR841Nv8, WR841Nv11
from root.base import BaseCommand
from root.iostream import get_pickle


class Command(BaseCommand):
    help = 'Connection which use PPPoE, it will reboot after configured successfully.'

    def add_args(self, parser: ArgumentParser):
        parser.add_argument('--host', default=None, help='TP-Link Router IP Address')
        parser.add_argument('-u', '--user', default='admin', help='Username Login, default is admin')
        parser.add_argument('-p', '--password', default='admin', help='Password Login, default is admin')
        parser.add_argument('-v', '--version', default='11', choices=[8, 11])

    def handle(self, *args, **kwargs):
        host = kwargs.get('host')
        version = kwargs.get('version')
        user = kwargs.get('user')
        password = kwargs.get('password')
        persists = get_pickle('db.pickle')
        assert (persists is not None), "Config Not Found"

        host = persists.get('host') if host is None else host
        try:
            tl = WR841Nv8(host, user, password) if version == '8' else WR841Nv11(host, user, password)
            tl.set_auth(persists.get('account'), persists.get('password'))
            tl.tag_vlan(True)
        except Exception as e:
            print(e)
