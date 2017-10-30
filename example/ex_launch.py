#! /usr/bin/env python
import roslaunch_api_wrapper as raw
import signal
import sys

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

def main():
    raw.LauncherStarter('turtle_tf','turtle_tf_demo.launch')
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C')
    signal.pause()

if __name__ == '__main__':
    main()