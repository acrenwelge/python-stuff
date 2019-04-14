from time import sleep

def report_status(signum, frame):
  global primes_list
  print("found %d primes so far" % len(primes_list))

def isprime(n):
  sleep(0.1)
  x=2
  while (x*x) <= n:
    if not n % x:
      return False
    x += 1
  return True

n=1
primes_list=[]

while True:
  if isprime(n):
    print("%d is prime" % n)
    primes_list.append(n)
    if len(primes_list) % 20 == 0:
      print("found %d primes so far" % len(primes_list))
  n+=1
