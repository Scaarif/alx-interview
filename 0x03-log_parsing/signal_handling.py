#!/usr/bin/python3
""" signal handling in action example """
# from time import sleep

# 1. default exception method...
# while True:
#     try:
#         print('.', end='', flush=True)
#         sleep(1)
#     except KeyboardInterrupt:
#         print('interrupted')
#         exit(0)

# 2. signal handling method... (allows multiple sigint calls - could be problematic)
# import sys
# import time
# import signal


# def interrupt_handler(signum, frame):
#     print(f'Handling signal {signum} ({signal.Signals(signum).name}).')

#     # do whatever...
#     time.sleep(1)
#     sys.exit(0)


# def main():
#     while True:
#         print('.', end='', flush=True)
#         time.sleep(0.3)


# if __name__ == '__main__':
#     signal.signal(signal.SIGINT, interrupt_handler)

#     main()

# 3. signal handling method... (prompt user to confirm signal interrupt) - still allows multiple interrupts
# import sys
# import time
# import signal
# from functools import partial


# def interrupt_handler(signum, frame, ask=True):
#     print(f'Handling signal {signum} ({signal.Signals(signum).name}).')
#     if ask:
#         signal.signal(signal.SIGINT, partial(interrupt_handler, ask=False))
#         # Instead of functools’ partial, we could also use a lambda expression like signal.signal(signal.SIGINT, lambda sig, frame: interrupt_handler(sig, frame, ask=False))
#         print('To confirm interrupt, press ctrl-c again.')
#         return

#     print('Cleaning/exiting...')
#     # do whatever...
#     time.sleep(1)
#     sys.exit(0)


# def main():
#     while True:
#         print('.', end='', flush=True)
#         time.sleep(0.3)


# if __name__ == '__main__':
#     signal.signal(signal.SIGINT, interrupt_handler)

#     main()

# 4. A simple way of stopping further calls to the handler is to reset the handler for the signal yet again
# - this time to ignore interrupts by using the SIG_IGN handler:
import sys
import time
import signal
from functools import partial


def interrupt_handler(signum, frame, ask=True):
    print(f'Handling signal {signum} ({signal.Signals(signum).name}).')
    if ask:
        signal.signal(signal.SIGINT, partial(interrupt_handler, ask=False))
        print('To confirm interrupt, press ctrl-c again.')
        return
    else:
        signal.signal(signum, signal.SIG_IGN)
    print('Cleaning/exiting...')
    # do whatever...
    time.sleep(1)
    sys.exit(0)


def main():
    while True:
        print('.', end='', flush=True)
        time.sleep(0.3)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, interrupt_handler)

    main()