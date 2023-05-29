import unittest
import animedata as ad
import os.path

class dict_checking_tests(unittest.TestCase):
    def test_check_dict(self):
        test_1 = {"anime_1":{"type": "anime", "anime_name": "anime_1"}}
        test_2 = {"anime_1":{"type": "unknown"}}
        self.assertTrue(ad.check_dict(test_1)[0] and not ad.check_dict(test_2)[0])


class lib_interaction_tests(unittest.TestCase):
    def test_get_ad_lib(self):
        ad.get_ad_lib()
        self.assertTrue(os.path.isfile(os.path.join(ad.dir_path,
                                                    "animedata_source.json")),
                        "Source file not found !")
        
    def test_get_ad_lib_content(self):
        ad.get_ad_lib()
        self.assertTrue(ad.check_dict(ad.get_ad_lib_content(True))[0])
        
    def test_save_json(self):
        test = {"anime_1" : {"type" : "anime", "anime_name" : "anime_1"}}
        ad.save_json(test)
        self.assertTrue(ad.check_dict(ad.get_ad_lib_content(False)))