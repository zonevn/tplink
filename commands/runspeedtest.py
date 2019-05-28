import speedtest

from root.base import BaseCommand
from argparse import ArgumentParser


class Command(BaseCommand):
    help = 'Check the connections of your network components'

    def add_args(self, parser: ArgumentParser):
        pass

    def handle(self, *args, **kwargs):
        d, u, p = self.__speedtest__()
        print("Ping: {}".format(p))
        print("Download: {:.2f} Kb/s".format(d / 1024))
        print("Upload: {:.2f} Kb/s".format(u / 1024))

    def __speedtest__(self):
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        return res["download"], res["upload"], res["ping"]
