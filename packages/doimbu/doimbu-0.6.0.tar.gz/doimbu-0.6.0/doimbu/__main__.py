import argparse

from doimbu import builder


def _copy_dict(dictionary: dict):
    return dictionary.copy() if dictionary else {}

class AppendKeyValueAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        dictionary = getattr(namespace, self.dest)
        dictionary = _copy_dict(dictionary)
        key, value = values.split('=')
        dictionary[key] = value.replace('"', '')
        setattr(namespace, self.dest, dictionary)


def parse_args(*args: str) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='doimbu - Docker Image Builder')
    parser.add_argument(
        '-d', '--default-variant',
        help='set which variant is the default'
             ' (the one that used for the tag suffix `latest`)')
    parser.add_argument(
        '-n', '--tag-namespace',
        help='tag namespace for the tag pattern:'
             ' [namespace]/[repository]:[version]-[variant]'
             ' | example: alexcarvalhotag-repositorydata/nginx-tini:1.2.1-ubi8'
    )
    parser.add_argument(
        '-r', '--tag-repository',
        help='tag repository'
    )
    parser.register('action', 'append_key_value', AppendKeyValueAction)
    parser.add_argument(
        '-b', '--build-arg',
        dest='build_args',
        action='append_key_value',
        help='tag repository'
    )
    parser.add_argument(
        '-o', '--only-default-variant',
        action='store_true',
        help='build only the default variant')
    parser.add_argument(
        '-l', '--tag-omit-latest',
        action='store_true',
        help='do not create at tag with the `latest` suffix'
             ' for the default variant')
    parser.add_argument(
        '-y', '--dry-run',
        action='store_true',
        help='print the commands on the execution plan'
             ', but do not execute them')

    return parser.parse_args(args) if args else parser.parse_args()


if __name__ == '__main__':
    _args = parse_args()

    builder.build(_args)
