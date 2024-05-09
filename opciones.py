from optparse import OptionParser
import sys

parser = OptionParser()

parser.add_option("--url", dest="url", help="Ingrese la URL.")
parser.add_option("-d", "--directory", dest="directorio", help="Ingrese el PATH")

(options, args) = parser.parse_args()

if options.url is None:
    parser.print_help()
    sys.exit()
else:
    print(options.url)
    print(options.directorio)
