import sys
from signal import *

def timeout_handler(signum, frame):
  raise IOError("User not responding")

def get_name():
  signal(SIGALRM, timeout_handler) # timeout does not work on Windows
  alarm(5)
  n=sys.stdin.readline()
  alarm(0)
  return n

print("enter your name: ", end = '')
sys.stdout.flush()
try:
  name = get_name()
except IOError:
  print("You did not reply, I'll call you 'Sleepy'")
  name = "Sleepy"

print("hello " + name)
