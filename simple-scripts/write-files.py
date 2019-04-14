import sys

print("this is written to stdout")
print("this is written to stderr", file = sys.stderr)
print("about to write files out1 and out2")

f = open("out1","w")
print("this is written to the out1 file", file=f)
f.close()

old_stdout = sys.stdout
with open("out2","w") as f:
  sys.stdout = f
  print("this is written to the out2 file")
sys.stdout = old_stdout
print("stdout is restored")
