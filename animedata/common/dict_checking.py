from copy import deepcopy
from animedata.common.metadata import ad_table

def check_dict(anime_dict: dict) -> tuple:
    """Check if the dictionnary is compatible with animedata's environment.

    Args:
        anime_dict (dict): dictionnary to check.

    Returns:
        tuple: tuple containing three main elements:
            - bool if the dictionnary is fully compatible.
            - corrected dictionnary.
            - list containing the corrupted keys of the original dict.
    """
    corrupted_keys = []
    dict_valid = True
    correct_dict = deepcopy(anime_dict)
    for element in anime_dict.keys():
        dict_element = anime_dict[element]
        try:
            if dict_element["type"] == "anime":
                if dict_element[ad_table["anime_name"]] != element:
                    corrupted_keys.append(element)
            elif dict_element["type"] == "metadata":
                del correct_dict[element]
            else:
                corrupted_keys.append(element)
        except KeyError:
            corrupted_keys.append(element)
    if len(corrupted_keys) != 0:
        for corrupted_anime in corrupted_keys:
            del correct_dict[corrupted_anime]
        dict_valid = False
    return dict_valid, correct_dict, corrupted_keys
