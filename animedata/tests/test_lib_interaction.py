import unittest
from animedata.common.lib_interactions import get_ad_lib, get_ad_lib_content
from animedata.common.metadata import ad_table
from animedata.common.dict_checking import check_dict


class test_lib_interaction(unittest.TestCase):
    def test_get_ad_lib(self):
        get_ad_lib()
        self.assertTrue(ad_table["source_file_path"],
                        "Source file not found !")

    def test_get_ad_lib_content(self):
        get_ad_lib()
        self.assertTrue(check_dict(get_ad_lib_content(True))[0])
