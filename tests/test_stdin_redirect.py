import unittest
import sys
import tempfile


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


def some_method_read_from_stdin():
    i = input()
    return i

class Test(unittest.TestCase):

    def setUp(self): pass  # nothing here for now

    def tearDown(self): pass  # nothing here for now


    def test(self):
        INP = EXP = '122'

        # make input file
        input_file = tempfile.mktemp()
        with open(input_file, 'w') as f: f.write(INP)

        # redirect :stdin to :input_file
        old_stdin = sys.stdin  # save it, in case we need to restore it
        sys.stdin = open(input_file)

        # call testee code
        ACTUAL_i = some_method_read_from_stdin()

        assert ACTUAL_i == EXP

        # restore stdin
        sys.stdin = old_stdin

