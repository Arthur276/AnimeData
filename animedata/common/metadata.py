import importlib.metadata
import os

ad_version = importlib.metadata.version("animedata")
dir_path = os.path.dirname(__file__)
ad_table = {
    "repository_url":
    "https://raw.githubusercontent.com/swarthur/animedata/",
    "source_file_name" : "animedata_source.json",
    "local_file_name" : "animedata_local.json",
    "source_file_path": "animedata\\resources\\animedata_source.json",
    "local_file_path": "animedata\\resources\\animedata_local.json",
    "anime_name": "anime_name",
    "seasons": "seasons",
    "episode_duration": "episode_duration",
    "episode_release_date": "episode_release_date",
    "episode_name": "episode_name"}