#!/usr/bin/python

import getopt
import sys

from Processors.IntegrationEngine import IntegrationEngine

def main(argv):
    input_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print 'Please specify input DICOM file by using -i <input_file> flag.'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <input_file>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg

    if input_file != '':
        IntegrationEngine(input_file)
    else:
        print 'Please specify input DICOM file by using -i <input_file> flag.'

if __name__ == "__main__":
    main(sys.argv[1:])