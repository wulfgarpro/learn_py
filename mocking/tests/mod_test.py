import unittest
import unittest.mock as mock
from package import mod_a
from package import mod_b
from mod import MyClass

class MyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _func():
        return 10

    @mock.patch('package.mod_a.func', side_effect=_func)
    def test_a(self, func_func):
        self.assertEqual(10, mod_a.func())

    @mock.patch('package.mod_a.func', side_effect=_func)
    def test_b(self, func_func):
        self.assertEqual(10, mod_b.go())

    @mock.patch('mod.MyClass.factory', return_value=None)
    def test_c(self, myclass_factory):
        self.assertEqual(None, MyClass.factory())
