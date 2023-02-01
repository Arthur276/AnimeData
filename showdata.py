"""Module to manage ShowData library."""

import json
import urllib.request
import urllib.error
import tomllib
import warnings
import os.path
from copy import deepcopy

dir_path = os.path.dirname(__file__)
showdata_table = {
    "repository_url":
    f"https://raw.githubusercontent.com/swarthur/showdata/",
    "source_file_name": "./showdata_source.json",
    "local_file_name": "./showdata_local.json",
    "key_show_name": "show_name",
    "key_seasons_episodes": "seasons_episodes",
    "key_episode_duration": "episode_duration",
    "key_episode_release_date": "episode_release_date",
    "key_episode_name": "episode_name"}

with open(os.path.join(dir_path, "./pyproject.toml"), mode="rb") as pypr:
    showdata_version = tomllib.load(pypr)["project"]["version"]
print("ShowData script version : ", showdata_version)


def get_showdata_lib(branch: str = "main"):
    """Download and replace local showdata library from Github.

    Args:
        branch (str, optional): select the target branch.
            Defaults to "main".
    """
    try:
        urllib.request.urlretrieve(
            showdata_table["repository_url"] +
            branch + "/" +
            showdata_table["source_file_name"][2:],
            os.path.join(dir_path, showdata_table["source_file_name"]))
    except urllib.error.HTTPError:
        if branch != "main":
            warnings.warn("Invalid Github URL : Fallback on main branch,\
database may not be as expected", ResourceWarning)
            get_showdata_lib()
        else:
            raise RuntimeError("Unable to get library from Github")


def get_showdata_lib_content(showdata_source: bool = False) -> dict:
    """Extract library data into a dictionnary.

    Args:
        showdata_source (bool, optional): Define if the data's
            source file is showdata's source file,
            otherwise it is a custom file. Defaults to False.

    Returns:
        dict: dictionnary containg library data
    """
    if showdata_source:
        target_file = showdata_table["source_file_name"]
    else:
        target_file = showdata_table["local_file_name"]
    with open(os.path.join(dir_path,
              target_file),
              encoding="utf-8") as showdata_json:
        showdata_dict = json.load(showdata_json)
        return showdata_dict


def show_lib_content():
    """Show the version of the library and the show available."""
    # STATUS : OK
    showdata_dict = get_showdata_lib_content()
    print("showdata library version :",
          showdata_dict["SHOWDATA-METADATA"]["showdata_version"],
          "#" + showdata_dict["SHOWDATA-METADATA"]["lib_subversion"])
    print("Shows available :")
    for element in showdata_dict.values():
        if element["type"] == "show":
            print(element[showdata_table["key_show_name"]])


def save_json(shows_dict: dict):
    """Save a dictionnary into a json file.

    Args:
        shows_dict (dict): Dictionnary containing shows data.
            Must be formatted with multi_shows_dict.
    """
    # STATUS : OK
    with open(os.path.join(dir_path, showdata_table['local_file_name']),
              "w",
              encoding="utf-8") as local_json:
        if not check_dict(shows_dict)[0]:
            warnings.warn(f"The dictionnary contains one or several \
corrupted key, ignoring it. Corrupted keys : {check_dict(shows_dict)[2]}")
        correct_dict = check_dict(shows_dict)[1]
        json_dict = {
            "SHOWDATA-METADATA": {
                "type": "metadata",
                "showdata_version": showdata_version},
            **correct_dict
            }
        json.dump(obj=json_dict, fp=local_json, ensure_ascii=False, indent=4)


def check_dict(shows_dict: dict) -> tuple:
    """Check if the dictionnary is compatible with showdata's environment.

    Args:
        shows_dict (dict): dictionnary to check.

    Returns:
        tuple: tuple containing three main elements:
            - bool if the dictionnary is fully compatible.
            - corrected dictionnary.
            - list containing the corrupted keys of the original dict.
    """
    corrupted_keys = []
    dict_valid = True
    correct_dict = deepcopy(shows_dict)
    for element in shows_dict.keys():
        dict_element = shows_dict[element]
        try:
            if dict_element["type"] == "show":
                if dict_element.get(showdata_table["key_show_name"]) != element:
                    corrupted_keys.append(element)
            elif dict_element["type"] == "metadata":
                corrupted_keys.append(element)
            else:
                corrupted_keys.append(element)
        except KeyError:
            corrupted_keys.append(element)
    if len(corrupted_keys) != 0:
        for corrupted_shows in corrupted_keys:
            del correct_dict[corrupted_shows]
        dict_valid = False
    return dict_valid, correct_dict, corrupted_keys
