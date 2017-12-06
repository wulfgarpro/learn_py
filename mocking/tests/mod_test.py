import time

import unittest
import unittest.mock as mock
from package import mod_a
from package import mod_b

import mod
#from mod import MyClass

class MyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _func():
        return 10

    #@mock.patch('package.mod_a.func' side_effect=_func)
    def test_a(self):
        with mock.patch('package.mod_a.func', return_value=10) as mock_a:
            self.assertEqual(10, mod_b.go())
            self.assertEqual(1, mock_a.call_count)

    @mock.patch('package.mod_a.func', side_effect=_func)
    def test_b(self, func_func):
        self.assertEqual(10, mod_b.go())

    @mock.patch('mod.MyClass.factory', return_value=None)
    def test_c(self, myclass_factory):
        self.assertEqual(None, mod.MyClass.factory())

    # mock sleep
    @mock.patch('time.sleep')
    def test_time(self, time_mock):
        self.assertRaises(TimeoutError, mod.MyClass.factory, None, time.time()) 

    # dont mock sleep
    # commented out since it's slow...
    #def test_time(self):
    #    mod.MyClass.factory(None)
