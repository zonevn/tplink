import importlib
import os
import sys


def fetch(command):
    commands = os.listdir(os.path.join(os.path.dirname(__file__), 'commands'))
    assert ('.'.join([command, 'py']) in commands), "{} not matched".format(command)
    module = importlib.import_module('commands.{}'.format(command))
    return module.Command()


def main():
    try:
        cmd = sys.argv[1]
    except IndexError:
        cmd = 'help'
        sys.argv.append(cmd)

    try:
        cmd = fetch(cmd)  # type:BaseCommand
        cmd.run(sys.argv)
    except Exception as e:
        print(f'{type(e)}: {e}')


if __name__ == '__main__':
    main()
