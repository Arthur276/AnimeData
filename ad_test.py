import animedata as ad

if __name__ == "__main__":
    ad.github_branch  = "dev-0.1/"
    ad.get_ad_lib()
    test_json = ad.load_json(True)
    del test_json["ANIMEDATA-METADATA"]
    print(ad.check_dict(test_json))
    ad.save_json(test_json)
    test_json_2 = ad.load_json(False)
    del test_json_2["ANIMEDATA-METADATA"]
    print(ad.check_dict(test_json_2))
    print(test_json_2 == test_json)
    