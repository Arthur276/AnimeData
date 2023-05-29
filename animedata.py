"""Module to manage AnimeData library."""

import json
import urllib.request
import urllib.error
import warnings
import importlib.metadata
import os.path
from copy import deepcopy

ad_version = importlib.metadata.version("animedata")
dir_path = os.path.dirname(__file__)
ad_table = {
    "repository_url":
    "https://raw.githubusercontent.com/swarthur/animedata/",
    "source_file_name": "./animedata_source.json",
    "local_file_name": "./animedata_local.json",
    "anime_name": "anime_name",
    "seasons": "seasons",
    "episode_duration": "episode_duration",
    "episode_release_date": "episode_release_date",
    "episode_name": "episode_name"}


def get_ad_lib(branch: str = "main"):
    """Download and replace local AnimeData library from Github.

    Args:
        branch (str, optional): select the target branch.
            Defaults to "main".
    """
    try:
        urllib.request.urlretrieve(
            ad_table["repository_url"] +
            branch + "/" +
            ad_table["source_file_name"][2:],
            os.path.join(dir_path, ad_table["source_file_name"]))
    except urllib.error.HTTPError:
        if branch != "main":
            warnings.warn("Invalid Github URL : Fallback on main branch,\
database may not act as expected", ResourceWarning)
            get_ad_lib()
        else:
            raise RuntimeError("Unable to get library from Github")


def get_ad_lib_content(ad_source: bool = False) -> dict:
    """Extract library data into a dictionnary.

    Args:
        ad_source (bool, optional): Define if the data's
            source file is AnimeData's source file,
            otherwise it is a custom file. Defaults to False.

    Returns:
        dict: dictionnary containg library data
    """
    if ad_source:
        target_file = ad_table["source_file_name"]
    else:
        target_file = ad_table["local_file_name"]
    with open(os.path.join(dir_path,
              target_file),
              encoding="utf-8") as ad_json:
        ad_dict = json.load(ad_json)
        return ad_dict


def show_lib_content():
    """Show the version of the library and the animes available."""
    # STATUS : OK
    ad_dict = get_ad_lib_content()
    print("AnimeData library version :",
          ad_dict["ANIMEDATA-METADATA"]["animedata_version"],
          "#" + ad_dict["ANIMEDATA-METADATA"]["lib_subversion"])
    print("Animes available :")
    for element in ad_dict.values():
        if element["type"] == "anime":
            print(element[ad_table["key_anime_name"]])


def save_json(anime_dict: dict):
    """Save a dictionnary into a json file.

    Args:
        anime_dict (dict): Dictionnary containing anime's data.
            Must be formatted with multi_anime_dict.
    """
    # STATUS : OK
    with open(os.path.join(dir_path, ad_table['local_file_name']),
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
