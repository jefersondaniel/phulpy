from .file import File
from glob import glob
import os
import fnmatch


class Source(object):
    def __init__(self, glob_patterns, read):
        self.__files = []

        files = []
        for pattern in glob_patterns:
            files = files + self.__find_patern(pattern)

        for file in files:
            self.__files.append(File(file, read=read))

    def __find_patern(self, pattern):
        if '**/' in pattern:
            explode = pattern.split('**/')
            path = explode[0]
            find = explode[1]

            results = [
                os.path.join(dirpath, f)
                for dirpath, dirnames, files in os.walk(path)
                for f in fnmatch.filter(files, find)
            ]
        else:
            results = glob(pattern)

        return [result for result in results if os.path.isfile(result)]

    def pipe(self, callback):
        callback(self)
        return self

    @property
    def files(self):
        return self.__files

    @files.setter
    def files(self, value):
        self.__files = value
