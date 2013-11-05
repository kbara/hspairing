import random
import unittest
from mergeseg import merge, arePathsSane

class TestMerge(unittest.TestCase):
    def testEmpty(self):
        assert(merge([]) == [])

    def testMergeOne(self):
        assert(merge(['ab', 'bc']) == ['abc'])

    def testMergeTwo(self):
        res = merge(['ab', 'bc', 'cd', 'xy'])
        res.sort()
        assert(res == ['abcd', 'xy'])

    def testBackwards(self):
        res = merge(['cd', 'bc', 'ab', 'xy'])
        res.sort()
        assert(res == ['abcd', 'xy'])

    def testJoinPaths(self):
        res = merge(['mn', 'op', 'no', 'xy'])
        res.sort()
        assert (res == ['mnop', 'xy'])

    def testSanity(self):
        assert(arePathsSane(['abc', 'xy']))
        assert(not arePathsSane(['abc', 'bd']))
        assert(not arePathsSane(['abc', 'cd']))
        assert(arePathsSane(merge(['ab', 'bc', 'cd', 'xy'])))

if __name__ == '__main__':
    unittest.main()

