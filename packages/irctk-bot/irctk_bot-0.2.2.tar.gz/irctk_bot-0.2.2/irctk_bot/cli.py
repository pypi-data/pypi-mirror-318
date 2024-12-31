import argparse
import asyncio
import importlib
import logging
import sys
import time
import tomllib

from irctk_bot.controller import Controller


def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        'irctk-bot', description='irctk bot', add_help=False
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-h', '--host')
    group.add_argument('-c', '--config', type=argparse.FileType('rb'))

    parser.add_argument('-m', '--module', action='append')
    parser.add_argument('-n', '--nick')
    parser.add_argument('-j', '--join', action='append')

    parser.add_argument('--verbose', action='store_true')
    return parser


def create_controller(args):
    host = None
    nick = 'bot'
    modules = set()
    channels = set()

    if args.config:
        config = tomllib.load(args.config)
        keys = set(config.keys())
        allowed_keys = set(['modules', 'host', 'nick', 'join'])
        for key in allowed_keys:
            if key in keys:
                keys.remove(key)
        if keys:
            print(f'Invalid fields in config: {keys}', file=sys.stderr)
            sys.exit(1)

        host = config['host']

        if 'nick' in config:
            nick = config['nick']

        if 'modules' in config:
            for module in config['modules']:
                modules.add(module)

        if 'join' in config:
            for channel in config['join']:
                channels.add(channel)

    if args.host:
        host = args.host

    if args.nick:
        nick = args.nick

    if args.join:
        for channel in args.join:
            channels.add(channel)

    if args.module:
        for module in args.module:
            modules.add(module)

    assert host
    controller = Controller(nick, host, channels)
    for module in modules:
        controller.add_module(importlib.import_module(module))

    return controller


def main() -> None:
    args = create_argument_parser().parse_args()

    if args.verbose:
        logging.basicConfig(level='DEBUG')
    else:
        logging.basicConfig(level='INFO')

    controller = create_controller(args)

    with asyncio.Runner() as runner:
        while True:
            try:
                runner.run(controller.connect())
            except Exception as e:
                print(e)

            # while not ideal, there does not appear to be public API to
            # allow us to differentiate between interrupt (abort process)
            # and the task exiting to trigger a reconnect.
            if getattr(runner, '_interrupt_count', 0) > 0:
                return

            time.sleep(2)
