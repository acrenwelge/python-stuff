from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--threshold",dest="threshold",type="int",default=90,help="Set threshold (%)")

(options, args) = parser.parse_args()

print("options: " + str(options))
print("args: " + str(args))
