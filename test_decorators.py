import unittest

import decorators

class TestDecoration(unittest.TestCase):
    def test_upper_case_example(self):
        self.assertEquals(decorators.greet("world"), 'HELLO WORLD')
