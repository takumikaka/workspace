# coding:UTF-8 -*-

import logging

logging.basicConfig(level = logging.DEBUG,
                    format = "[%(asctime)s] %(levelname)s [%(funcName)s:%(filename)s,%(lineno)d] %(message)s",
                    datefmt = "%Y-%m-%d %H:%M:%S",
                    filename = "log.txt",
                    filemode = "a"
                    )

if __name__ == "__main__":
    logging.info("hello")
