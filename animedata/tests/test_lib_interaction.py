import unittest
import os
from animedata.common import lib_interactions as adlib
from animedata.common import saving_process as adsave
from animedata.common import metadata as admeta
from animedata.common import dict_checking as adcheck


class test_lib_interaction(unittest.TestCase):
    def test_get_ad_lib(self):
        adlib.get_ad_lib()
        self.assertTrue(os.path.isfile(admeta.ad_table["source_file_path"]),
                        "Source file not found !")
        
    def test_get_ad_lib_content(self):
        adlib.get_ad_lib()
        self.assertTrue(adcheck.check_dict(adlib.get_ad_lib_content(True))[0])
        
    def test_save_json(self):
        test = {"anime_1" : {"type" : "anime", "anime_name" : "anime_1"}}
        adsave.save_json(test)
        self.assertTrue(adcheck.check_dict(adlib.get_ad_lib_content(False)))