#!/usr/bin/python

import sys, getopt
from Processors.IntegrationEngine import IntegrationEngine

def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
   except getopt.GetoptError:
      print 'Please specify input DICOM file by using -i <inputfile> flag.'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg

   if inputfile != '':
       IntegrationEngine(inputfile)
   else:
       print 'Please specify input DICOM file by using -i <inputfile> flag.'

if __name__ == "__main__":
   main(sys.argv[1:])