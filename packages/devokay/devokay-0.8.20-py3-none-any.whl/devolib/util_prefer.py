# -*- coding: UTF-8 -*-
# python3

from devolib.util_fs import path_home, path_join_one

CONFIG_DIR = ".devo"
CONFIG_FILE = "conf.json"

profile_dir = path_home()
conf_dir = path_join_one(profile_dir, CONFIG_DIR)
conf_file = path_join_one(conf_dir, CONFIG_FILE)
