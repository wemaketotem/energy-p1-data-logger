#!/usr/bin/python

import sys
import serial
import argparse

def create_parser():
    parser = argparse.ArgumentParser(
        description='Run a smart meter data logger'
    )

    parser.add_argument(
        'port', metavar='port', type=str,
        help='Serial port to use'
    )

    parser.add_argument(
        '-v', '--version', type=float, default=2.2, choices=[2.2, 4.0],
        help='DSMR version'
    )

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        if args.version == 2.2:
            # Connect to serial port at 9600 baud with 7 data bits per byte, no parity checking and 2 stop bits
            serial_port = serial.Serial(args.port, 9600, bytesize=serial.SEVENBITS, parity=serial.PARITY_NONE, stopbits=2)
        else:
            # Connect to serial port at 115200 baud with 8 data bits per byte, no parity checking and 1 stop bit
            serial_port = serial.Serial(args.port, 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=1)

    except serial.SerialException as e:
        print e

    else:
        print "Opened: ", serial_port.name

        while True:
            sys.stdout.write(serial_port.readline())

if __name__ == '__main__':
    main()
