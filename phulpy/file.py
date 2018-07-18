import os


class File(object):

    def __init__(self, relative_path, read):
        self.__content = ''

        self.__relative_path = relative_path
        self.__real_path = os.path.realpath(relative_path)
        self.__name = os.path.basename(relative_path)
        if read:
            self.__read_content()

    def __read_content(self):
        self.__content = open(self.__relative_path, 'r').read()

    @property
    def content(self):
        if '' is self.__content:
            self.__read_content()

        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    @property
    def relative_path(self):
        return self.__relative_path

    @relative_path.setter
    def relative_path(self, value):
        self.__relative_path = value

    @property
    def real_path(self):
        return self.__real_path

    @real_path.setter
    def real_path(self, value):
        self.__real_path = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return self.__relative_path
