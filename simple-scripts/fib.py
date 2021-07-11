# returns the nth fibonacci number
def getNth(n):
  a = 1
  b = 1
  if n == 1 or n == 2:
    return a
  else:
    for x in range(2,n):
      tmp = a
      a = a + b
      b = tmp
      print(a, b)
    return a
