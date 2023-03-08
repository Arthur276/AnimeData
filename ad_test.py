import animedata as ad


def test_get_lib():
    ad.get_ad_lib("main")
    test_json = ad.get_ad_lib_content(True)
    del test_json["ANIMEDATA-METADATA"]
    print(ad.check_dict(test_json))
    print("GET-LIB : OK")
    return ad.check_dict(test_json)[1]

def test_save_process():
    ad.save_json(test_get_lib())
    test_json = ad.get_ad_lib_content(False)
    del test_json["ANIMEDATA-METADATA"]
    print(ad.check_dict(test_json))
    print(test_json == test_get_lib())
    print("SAVE-PROCESS : OK")

if __name__ == "__main__":
    test_get_lib()
    test_save_process()