import unittest
from animedata.common import dict_checking as ad


class test_dict_checking(unittest.TestCase):
    def test_check_dict(self):
        test_1 = {"anime_1": {"type": "anime", "anime_name": "anime_1"}}
        test_2 = {"anime_1": {"type": "unknown"}}
        self.assertTrue(
            ad.check_dict(test_1)[0]
            and not ad.check_dict(test_2)[0])
