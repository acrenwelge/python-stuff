# Demonstrate piping into and out of a child process

from subprocess import Popen, PIPE
import random

sorter = Popen(["cat", "-n"], stdin=PIPE, stdout=PIPE)

# Write 10 random integers to the sorter's input
# this works for 10 numbers but will hang for
# much larger range due to deadlock
for i in range(10):
  sorter.stdin.write(("%d\n" % random.randrange(100)).encode())

# Without the .close() below, this will hang
# because the sorter will never see EOF on its standard input
sorter.stdin.close()

for line in sorter.stdout:
  print(line.decode(), end = '')

