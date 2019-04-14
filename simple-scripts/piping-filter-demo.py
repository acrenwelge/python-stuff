from subprocess import Popen, PIPE

# store the output from the shell command ls -l in a variable
lister = Popen(["ls", "-l"],stdout=PIPE)

# iterate over lister variable to filter piped results
for bytes in lister.stdout:
  line = bytes.decode() #decode from bytes to string
  if line.startswith("total"):
    continue
  splitline = line.split()
  if int(splitline[4]) > 300:
    print(splitline[8]) # show files bigger than 300 bytes
