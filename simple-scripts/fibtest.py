import unittest
import fib 

class FibTest(unittest.TestCase):

  def testOne(self):
    self.assertEqual(1, fib.getNth(1))

  def testTwo(self):
    self.assertEqual(1, fib.getNth(2))
  
  def testFive(self):
    self.assertEqual(5, fib.getNth(5))

  def testEight(self):
    self.assertEqual(21, fib.getNth(8))

if __name__ == '__main__':
  unittest.main()
