# coding:UTF-8 -*-

import logging
import os


prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log_file = os.path.join(prj_path, "log", "log.txt")
data_file = os.path.join(prj_path, "data", "china-city-list.xlsx")


logging.basicConfig(level=logging.DEBUG,
                    format="[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s %(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H: %M: %S",
                    filename=log_file,
                    filemode="a")
