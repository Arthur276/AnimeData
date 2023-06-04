import json
import warnings
from animedata.common.metadata import ad_table, ad_version
from animedata.common.dict_checking import check_dict


def save_json(anime_dict: dict):
    """Save a dictionnary into a json file.

    Args:
        anime_dict (dict): Dictionnary containing anime's data.
            Must be formatted with multi_anime_dict.
    """
    with open(ad_table["local_file_path"],
              "w",
              encoding="utf-8") as local_json:
        if not check_dict(anime_dict)[0]:
            warnings.warn(f"The dictionnary contains one or several \
corrupted key, ignoring it. Corrupted keys : {check_dict(anime_dict)[2]}")
        correct_dict = check_dict(anime_dict)[1]
        json_dict = {
            "ANIMEDATA-METADATA": {
                "type": "metadata",
                "animedata_version": ad_version},
            **correct_dict
            }
        json.dump(obj=json_dict, fp=local_json, ensure_ascii=False)