import watchdata as wd

if __name__ == "__main__":
    wd.get_wd_lib("feat/check-dict")
    test_json = wd.get_wd_lib_content(True)
    del test_json["WATCHDATA-METADATA"]
    print(wd.check_dict(test_json))
    wd.save_json(test_json)
    test_json_2 = wd.get_wd_lib_content(False)
    del test_json_2["WATCHDATA-METADATA"]
    print(wd.check_dict(test_json_2))
    print(test_json_2 == test_json)
