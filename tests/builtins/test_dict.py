from ..utils import BuiltinFunctionTestCase
from ..utils import TranspileTestCase


class DictTests(TranspileTestCase):

    def test_keys(self):
        d = {}
        self.assertEqual(set(d.keys()), set())
        d = {'a': 1, 'b': 2}
        k = d.keys()
        self.assertEqual(set(k), {'a', 'b'})
        self.assertIn('a', k)
        self.assertIn('b', k)
        self.assertIn('a', d)
        self.assertIn('b', d)
        self.assertRaises(TypeError, d.keys, None)
        self.assertEqual(repr(dict(a=1).keys()), "dict_keys(['a'])")


class BuiltinDictFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["dict"]
