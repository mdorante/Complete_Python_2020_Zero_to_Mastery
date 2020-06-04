import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        '''docstring #1'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        '''docstring #2'''
        test_param2 = 10
        result = main.do_stuff(test_param2)
        self.assertEqual(result, 3)

    def test_do_stuff3(self):
        '''passing \'askj\' as a param and expecting a ValueError'''
        test_param3 = 'askj'
        result = main.do_stuff(test_param3)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff4(self):
        '''passing \'None\' as a param and expecting \'please enter a number\''''
        test_param4 = None
        result = main.do_stuff(test_param4)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff5(self):
        '''passing an empty string, expecting \'please enter a number\''''
        test_param5 = ''
        result = main.do_stuff(test_param5)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff6(self):
        '''passing 0 and expecting 5'''
        test_param6 = 0
        result = main.do_stuff(test_param6)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()

# Output:
# .F....
# ======================================================================
# FAIL: test_do_stuff2 (__main__.TestMain)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/manuel/gitProjects/python/Complete_Python_Developer_2020/Testing_In_Python/test.py", line 15, in test_do_stuff2
#     self.assertEqual(result, 3)
# AssertionError: 15 != 3

# ----------------------------------------------------------------------
# Ran 6 tests in 0.001s

# FAILED (failures=1)

# NOTE: In the first line of output, we can see that the first test was OK '.',
# the second test failed 'F', and tests 3-6 were OK '.'
# The we can see what the fail was in the second test, it failed because when we pass 10 as a param
# to the do_stuff function from main which adds 5 to it, it should return 15, not 3

# The third test was OK because we checked if result was an object of the ValueError class, and it was
# because we caught the exception after trying to convert a string to an int and returned err,
#  which is an object of the ValueError class


# NOTE: If we have multiple test files, we can run all of them by running 'pyton3 -m unittest'
# We can use -v 'verbose' just like in other linux commands

# Let's see what happens if we enter the 'python3.8 -m unittest -v' command:
# Output:
# test_do_stuff (test.TestMain)
# docstring #1 ... about to test a function
# ok
# test_do_stuff2 (test.TestMain)
# docstring #2 ... about to test a function
# FAIL
# test_do_stuff3 (test.TestMain)
# passing 'askj' as a param and expecting a ValueError ... about to test a function
# ok
# test_do_stuff4 (test.TestMain)
# passing 'None' as a param and expecting 'please enter a number' ... about to test a function
# ok
# test_do_stuff5 (test.TestMain)
# passing an empty string, expecting 'please enter a number' ... about to test a function
# ok
# test_do_stuff6 (test.TestMain)
# passing 0 and expecting 5 ... about to test a function
# ok

# ======================================================================
# FAIL: test_do_stuff2 (test.TestMain)
# docstring #2
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/manuel/gitProjects/python/Complete_Python_Developer_2020/Testing_In_Python/test.py", line 19, in test_do_stuff2
#     self.assertEqual(result, 3)
# AssertionError: 15 != 3

# ----------------------------------------------------------------------
# Ran 6 tests in 0.000s

# FAILED (failures=1)
