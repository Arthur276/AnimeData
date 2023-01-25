"""Module to manage watchdata library."""

import json
import urllib.request
import urllib.error
import tomllib
import warnings
import os.path
from copy import deepcopy

dir_path = os.path.dirname(__file__)
wd_table = {
    "repository_url":
    f"https://raw.githubusercontent.com/swarthur/watchdata/",
    "source_file_name": "./watchdata_source.json",
    "local_file_name": "./watchdata_local.json",
    "key_series_name": "series_name",
    "key_seasons_episodes": "seasons_episodes",
    "key_episode_duration": "episode_duration",
    "key_episode_release_date": "episode_release_date",
    "key_episode_name": "episode_name"}

with open(os.path.join(dir_path, "./pyproject.toml"), mode="rb") as pypr:
    wd_version = tomllib.load(pypr)["project"]["version"]
print("watchdata script version : ", wd_version)


def get_wd_lib(branch: str = "main"):
    """Download and replace local watchdata library from Github.

    Args:
        branch (str, optional): select the target branch.
            Defaults to "main".
    """
    try:
        urllib.request.urlretrieve(
            wd_table["repository_url"] +
            branch + "/" +
            wd_table["source_file_name"][2:],
            os.path.join(dir_path, wd_table["source_file_name"]))
    except urllib.error.HTTPError:
        if branch != "main":
            warnings.warn("Invalid Github URL : Fallback on main branch,\
database may not be as expected", ResourceWarning)
            get_wd_lib()
        else:
            raise RuntimeError("Unable to get library from Github")


def get_wd_lib_content(wd_source: bool = False) -> dict:
    """Extract library data into a dictionnary.

    Args:
        wd_source (bool, optional): Define if the data's
            source file is watchdata's source file,
            otherwise it is a custom file. Defaults to False.

    Returns:
        dict: dictionnary containg library data
    """
    if wd_source:
        target_file = wd_table["source_file_name"]
    else:
        target_file = wd_table["local_file_name"]
    with open(os.path.join(dir_path,
              target_file),
              encoding="utf-8") as wd_json:
        wd_dict = json.load(wd_json)
        return wd_dict


def show_lib_content():
    """Show the version of the library and the series available."""
    # STATUS : OK
    wd_dict = get_wd_lib_content()
    print("watchdata library version :",
          wd_dict["WATCHDATA-METADATA"]["watchdata_version"],
          "#" + wd_dict["WATCHDATA-METADATA"]["lib_subversion"])
    print("Series available :")
    for element in wd_dict.values():
        if element["type"] == "series":
            print(element[wd_table["key_anime_name"]])


def save_json(series_dict: dict):
    """Save a dictionnary into a json file.

    Args:
        series_dict (dict): Dictionnary containing series data.
            Must be formatted with multi_series_dict.
    """
    # STATUS : OK
    with open(os.path.join(dir_path, wd_table['local_file_name']),
              "w",
              encoding="utf-8") as local_json:
        if not check_dict(series_dict)[0]:
            warnings.warn(f"The dictionnary contains one or several \
corrupted key, ignoring it. Corrupted keys : {check_dict(series_dict)[2]}")
        correct_dict = check_dict(series_dict)[1]
        json_dict = {
            "WATCHDATA-METADATA": {
                "type": "metadata",
                "watchdata_version": wd_version},
            **correct_dict
            }
        json.dump(obj=json_dict, fp=local_json, ensure_ascii=False, indent=4)


def check_dict(series_dict: dict) -> tuple:
    """Check if the dictionnary is compatible with watchdata's environment.

    Args:
        series_dict (dict): dictionnary to check.

    Returns:
        tuple: tuple containing three main elements:
            - bool if the dictionnary is fully compatible.
            - corrected dictionnary.
            - list containing the corrupted keys of the original dict.
    """
    corrupted_keys = []
    dict_valid = True
    correct_dict = deepcopy(series_dict)
    for element in series_dict.keys():
        dict_element = series_dict[element]
        try:
            if dict_element["type"] == "series":
                if dict_element.get(wd_table["key_series_name"]) != element:
                    corrupted_keys.append(element)
            elif dict_element["type"] == "metadata":
                corrupted_keys.append(element)
            else:
                corrupted_keys.append(element)
        except KeyError:
            corrupted_keys.append(element)
    if len(corrupted_keys) != 0:
        for corrupted_series in corrupted_keys:
            del correct_dict[corrupted_series]
        dict_valid = False
    return dict_valid, correct_dict, corrupted_keys
