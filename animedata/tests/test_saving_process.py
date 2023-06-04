import unittest
from animedata.common.saving_process import save_json
from animedata.common.dict_checking import check_dict
from animedata.common.lib_interactions import get_ad_lib_content

class test_saving_process(unittest.TestCase):
    def test_save_json(self):
        test = {"anime_1" : {"type" : "anime", "anime_name" : "anime_1"}}
        save_json(test)
        self.assertTrue(check_dict(get_ad_lib_content(False)))