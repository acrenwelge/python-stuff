def lone_sum(a, b, c):
  myset = set()
  sum = 0
  for num in myset:
    if myset.issuperset(set([num])):
      pass
    else:
      sum += num
    myset.add(num)
  return sum
