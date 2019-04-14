from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--threshold",dest="threshold",type="int",default=90,help="Set threshold (%)")

(option, args) = parser.parse_args()

print("singleshot is %r" % options.singleshot)
