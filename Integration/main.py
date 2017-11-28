import getopt
import sys
from Processors.IntegrationProcessor import IntegrationProcessor
import RequestHandler

def argument_error_print():
    print 'DICOM processor requires a path to the root folder, which should contain other folders and files grouped as follows:'
    print '|- Root (a Patient folder)'
    print '   |- Studies'
    print '      |- Series'
    print '         |- Instances (.dcm files)'
    print 'All DICOM files are processed according to config file provided.'
    print '\033[91m[!] Please specify the root path by using -i <root_folder_path> flag.'
    print '\033[91m[!] Please specify the configuration file by using -c <path_to_config_file> flag.'
    print '\033[91m[!] Please specify the output file by using -o <path_to_output_file> flag.'

def main(argv):
    root_path = ''
    config_path = ''
    output_path = ''

    try:
        opts, args = getopt.getopt(argv, "hi:c:o:", ["path=", "config=", "output="])
    except getopt.GetoptError:
        argument_error_print()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            argument_error_print()
            sys.exit()
        elif opt in ("-i", "--path"):
            root_path = arg
        elif opt in ("-c", "--config"):
            config_path = arg
        elif opt in ("-o", "--output"):
            output_path = arg

    if root_path != '' and config_path != '':
        IntegrationProcessor(config_path, root_path, output_path).integrate()
    else:
        argument_error_print()

    RequestHandler.RequestHandler()

if __name__ == "__main__":
    main(sys.argv[1:])
