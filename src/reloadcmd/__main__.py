#!/usr/bin/env python

import os
import time
import coloredlogs
import logging
import argparse
from watchdog.observers import Observer
from reloadcmd.monitor import Monitor

log_level = logging.DEBUG

parser = argparse.ArgumentParser(description='Restarts process when any files / directory changes')
parser.add_argument('-d', '--debug', dest='debug',
    help='Debug mode')
parser.add_argument('-p', '--path', default=os.getcwd(), dest='path',
    help='Which directory to watch for changes')
parser.add_argument('-e', '--extension', default=[".go", ".toml"], dest='file_ext', nargs='*',
    help="Which file extensions to listen for")
parser.add_argument('-c', '--command', required=True, dest='command',
    help='Command to be executed')

args = parser.parse_args()


def main():
    coloredlogs.install(level=log_level,
                        fmt='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    os.chdir(args.path)

    event_handler = Monitor(args.command, args.file_ext)
    observer = Observer()
    observer.schedule(event_handler, args.path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        event_handler.executor.kill()
        observer.stop()

    observer.join()
    logging.debug("Exiting...")


if __name__ == "__main__":
    main()
