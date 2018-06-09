# -*- coding: utf-8 -*-

import os
from processers.get_cwd import getCwd

class readFilename(object):

    def __init__(self):
        self.get_cwd = getCwd()
        self.path_one = self.get_cwd.run()
        self.file_dir = self.path_one + 'sources/files'

    def run(self):
        for files in os.walk(self.file_dir):
            for file_list in files:
                pass
        del[file_list[0]]
        return file_list

def main():
    action = readFilename()
    action.run()

if __name__ == '__main__':
    main()
