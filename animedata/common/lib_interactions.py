import urllib.request
import warnings
import json
from animedata.common.metadata import ad_table


def get_ad_lib(branch: str = "main"):
    """Download and replace local AnimeData library from Github.

    Args:
        branch (str, optional): select the target branch.
            Defaults to "main".
    """
    try:
        urllib.request.urlretrieve(
            ad_table["repository_url"] +
            branch + "/" + "animedata/resources/" +
            ad_table["source_file_name"],
            ad_table["source_file_path"])
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
        target_file = ad_table["source_file_path"]
    else:
        target_file = ad_table["local_file_path"]
    with open(target_file, encoding="utf-8") as ad_json:
        ad_dict = json.load(ad_json)
    return ad_dict


def show_lib_content(ad_source):
    """Show the version of the library and the animes available."""
    ad_dict = get_ad_lib_content(ad_source)
    print("AnimeData library version :",
          ad_dict["ANIMEDATA-METADATA"]["animedata_version"],
          "#" + ad_dict["ANIMEDATA-METADATA"]["lib_subversion"])
    print("Animes available :")
    for element in ad_dict.values():
        if element["type"] == "anime":
            print(element[ad_table["anime_name"]])
