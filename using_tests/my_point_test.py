import unittest
from my_point import Point

# NB the best tests are written from a really thorough specification

class testPoint(unittest.TestCase):
    '''here are the tests for the Point class'''
    def setUp(self):
        '''this method will be run before each test'''
        self.point = Point(3, 5) # a sensible isntance to use in our tests

    # declare some independent tests
    def testMoveBy_A(self):
        self.point.moveBy(-5, -2)
        self.assertEqual(self.point.display(), (-2, 3))
    def testMoveBy_B(self):
        self.point.moveBy(5, 2)
        self.assertEqual(self.point.x, 8)
        self.assertEqual(self.point.y, 7)
    def testHypot(self):
        '''the hypotenuse should be correctly derived'''
        self.point.moveBy(0, -1) # (3, 4)
        r = self.point.hypot()
        self.assertAlmostEqual(r, 5.00, places=2)
    def testPosNegHypot(self):
        self.positive = Point(3,4)
        self.negative = Point(-3,-4)
        self.assertEqual(self.positive.hypot(), self.negative.hypot())

if __name__ == '__main__':
    unittest.main() # invoke our tests