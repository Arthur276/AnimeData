import animedata as ad

if __name__ == "__main__":
    ad.get_ad_lib("feat/check-dict")
    test_json = ad.get_ad_lib_content(True)
    del test_json["ANIMEDATA-METADATA"]
    print(ad.check_dict(test_json))
    ad.save_json(test_json)
    test_json_2 = ad.get_ad_lib_content(False)
    del test_json_2["ANIMEDATA-METADATA"]
    print(ad.check_dict(test_json_2))
    print(test_json_2 == test_json)
