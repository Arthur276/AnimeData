"""Module to manage animedata library."""

import json
import urllib.request
import tomli
import warnings
import os

script_path = os.path.dirname(__file__)
dev_mode = False
ad_table = {
    "dev_branch": "dev-0.1/",
    "main_branch": "main/",
    "repository_url":
    "https://raw.githubusercontent.com/swarthur/animedata/",
    "source_file_name": "./animedata_source.json",
    "local_file_name": "./animedata_local.json",
    "key_anime_name": "anime_name",
    "key_seasons_episodes": "seasons_episodes",
    "key_episode_duration": "episode_duration",
    "key_episode_release_date": "episode_release_date",
    "key_episode_name": "episode_name"}

with open(os.path.join(script_path,"./pyproject.toml"), mode="rb") as pypr:
    ad_version = tomli.load(pypr)["project"]["version"]
print("AnimeData script version : ", ad_version)


def update_anime_lib():
    """Download and replaces animedata_source.json file from Github."""
    # STATUS : OK
    if dev_mode:
        urllib.request.urlretrieve(
            ad_table["repository_url"] +
            ad_table["dev_branch"] +
            ad_table["source_file_name"],
            ad_table["source_file_name"])
    else:
        urllib.request.urlretrieve(
            ad_table["repository_url"] +
            ad_table["main_branch"] +
            ad_table["source_file_name"],
            ad_table["source_file_name"])
    with open(os.path.join(script_path,ad_table["source_file_name"]), encoding="utf-8") as ad_json:
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

    Raises:
        SyntaxError: Error when the dictionnary is not correctly formatted
    """
    # STATUS : OK
    with open(os.path.join(script_path,ad_table['local_file_name']),
              "w",
              encoding="utf-8") as local_json:
        for anime in anime_dict.values():
            if anime["type"] != "anime":
                raise SyntaxError("The dictionnary is not correctly \
                                  formated. Use format_dict()")
        json_dict = {
            "ANIMEDATA-METADATA": {
                "type": "metadata",
                "animedata_version": ad_version},
            **anime_dict}
        json.dump(obj=json_dict, fp=local_json, ensure_ascii=False)


def load_json_dict(ad_source: bool = False) -> dict:
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
    with open(os.path.join(script_path,target_file), "r", encoding="utf-8") as ad_json:
        anime_dict = json.load(ad_json)
    return anime_dict
