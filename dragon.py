#!/usr/bin/env python
# Copyright (C) 2010-2013 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import sys
import gtk
import logging
import threading
import argparse

try:
    from lib.dragon.common.logo import logo
    from lib.dragon.common.constants import CUCKOO_VERSION
    from lib.dragon.common.exceptions import CuckooCriticalError, CuckooDependencyError
    from lib.dragon.core.startup import *
    from lib.dragon.core.scheduler import Scheduler
except (CuckooDependencyError, ImportError) as e:
    sys.exit("ERROR: Missing dependency: %s" % e)

log = logging.getLogger()

def start_loop_thread():
    global gtkthread

    gtk.gdk.threads_init()
    gtkthread = threading.Thread(target=gtk.mainloop)
    gtkthread.daemon = True
    gtkthread.start()

def main():
    logo()
    check_working_directory()
    check_configs()
    check_version()
    create_structure()
    start_loop_thread()

    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--quiet", help="Display only error messages", action="store_true", required=False)
    parser.add_argument("-d", "--debug", help="Display debug messages", action="store_true", required=False)
    parser.add_argument("-v", "--version", action="version", version="You are running Dragon Sandbox %s" % CUCKOO_VERSION)
    parser.add_argument("-a", "--artwork", help="Show artwork", action="store_true", required=False)
    args = parser.parse_args()

    if args.artwork:
        import time
        try:
            while True:
                time.sleep(1)
                logo()
        except KeyboardInterrupt:
            return

    init_logging()

    if args.quiet:
        log.setLevel(logging.WARN)
    elif args.debug:
        log.setLevel(logging.DEBUG)

    init_modules()

    try:
        sched = Scheduler()
        sched.start()
    except KeyboardInterrupt:
        sched.stop()

if __name__ == "__main__":
    try:
        main()
    except CuckooCriticalError as e:
        message = "%s: %s" % (e.__class__.__name__, e)
        if len(log.handlers) > 0:
            log.critical(message)
        else:
            sys.stderr.write("%s\n" % message)

        sys.exit(1)
