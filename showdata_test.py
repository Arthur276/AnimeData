import showdata as sdata

if __name__ == "__main__":
    sdata.get_showdata_lib("feat/check-dict")
    test_json = sdata.get_showdata_lib_content(True)
    del test_json["SHOWDATA-METADATA"]
    print(sdata.check_dict(test_json))
    sdata.save_json(test_json)
    test_json_2 = sdata.get_showdata_lib_content(False)
    del test_json_2["SHOWDATA-METADATA"]
    print(sdata.check_dict(test_json_2))
    print(test_json_2 == test_json)
