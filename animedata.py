"""Module to manage animedata library."""

import json
import urllib.request
import tomli
import warnings
import os.path
from copy import deepcopy

dir_path = os.path.dirname(__file__)
github_branch = "main/"
ad_table = {
    "repository_url":
    f"https://raw.githubusercontent.com/swarthur/animedata/",
    "source_file_name": "./animedata_source.json",
    "local_file_name": "./animedata_local.json",
    "key_anime_name": "anime_name",
    "key_seasons_episodes": "seasons_episodes",
    "key_episode_duration": "episode_duration",
    "key_episode_release_date": "episode_release_date",
    "key_episode_name": "episode_name"}

with open(os.path.join(dir_path,"./pyproject.toml"), mode="rb") as pypr:
    ad_version = tomli.load(pypr)["project"]["version"]
print("AnimeData script version : ", ad_version)


def update_anime_lib():
    """Download and replaces animedata_source.json file from Github."""
    # STATUS : OK
    urllib.request.urlretrieve(
        ad_table["repository_url"] +
        github_branch +
        ad_table["source_file_name"][2:],
        os.path.join(dir_path,ad_table["source_file_name"]))
    with open(os.path.join(dir_path,ad_table["source_file_name"]), encoding="utf-8") as ad_json:
        main_dict = json.load(ad_json)
        print("AnimeData library version :" +
              main_dict["ANIMEDATA-METADATA"]["animedata_version"],
              "#" +
              main_dict["ANIMEDATA-METADATA"]["lib_subversion"])
        print("Animes downloaded from Github :")
        for element in main_dict.values():
            if element["type"] == "anime":
                print(element[ad_table["key_anime_name"]])


def save_json(anime_dict: dict):
    """Save a dictionnary into a json file.

    Args:
        anime_dict (dict): Dictionnary containing anime's data.
            Must be formatted with multi_anime_dict.
    """
    # STATUS : OK
    with open(os.path.join(dir_path,ad_table['local_file_name']),
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
        json.dump(obj=json_dict, fp=local_json, ensure_ascii=False, indent= 4)


def load_json(ad_source: bool = False) -> dict:
    """Load data from a json file containing animes' data.

    Args:
        ad_source (bool, optional): Define if the data's
            source file is animedata's source file,
            otherwise it is a custom file. Defaults to False.

    Returns:
        dict: dictionnary containing anime's data.
    """
    # STATUS : OK
    if ad_source:
        target_file = ad_table["source_file_name"]
    else:
        target_file = ad_table["local_file_name"]
    with open(os.path.join(dir_path,target_file), "r", encoding="utf-8") as ad_json:
        anime_dict = json.load(ad_json)
    return anime_dict

def check_dict(anime_dict:dict) -> tuple:
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
                if dict_element.get(ad_table["key_anime_name"]) != element:
                    corrupted_keys.append(element)
            elif dict_element["type"] == "metadata":
                corrupted_keys.append(element)
            else:
                corrupted_keys.append(element)
        except KeyError:
            corrupted_keys.append(element)
    if len(corrupted_keys) != 0:
        for corrupted_anime in corrupted_keys:
            del correct_dict[corrupted_anime]
        dict_valid = False
    return dict_valid, correct_dict, corrupted_keys
