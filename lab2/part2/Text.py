import os  # os module provides functions for interacting with the operating system
import re  # regular expressions module


class Text:
    """
    Class Text used to perform statistical processing of a text file

    Attributes
    ----------
    __chars: int
        the number of chars in text
    __words: int
        the number of words in text
    __sentences: int
        the number of sentences in text
    __file: str
        the name of file with text
    __text: str
        text from file

    Methods
    -------
    chars()
        counts number of chars in text
    words()
        counts number of words in text
    sentences
        counts number of words in text
    counter(*args)
        calls methods chars(), words(), sentences() depending on the user's choice
    """
    def __init__(self, file):
        """
        Parameters
        ----------
        file: str
            the name of file with text
        """
        self.__chars = 0
        self.__words = 0
        self.__sentences = 0
        self.__file = file
        self.__text = ''

    def chars(self):
        """Counts and returns number of chars in text"""
        return len(self.__text)

    def words(self):
        """Counts and returns number of words in text"""
        return len(re.findall(r"[\s'.,!?]+", self.__text))

    def sentences(self):
        """Counts and returns number of sentences in text"""
        return len(re.findall(r'[.!?]+', self.__text))

    def counter(self, *args):
        """Calls methods chars(), words(), sentences() depending on the user's choice"""
        if not os.path.isfile(self.__file):  # checking whether the specified path is an existing file or not
            raise OSError('Cannot open file!')
        else:
            f = open(self.__file, 'r')
            self.__text = f.read()
            if args:
                for i in args:
                    if i == 'c':
                        self.__chars = self.chars()
                    elif i == 'w':
                        self.__words = self.words()
                    elif i == 's':
                        self.__sentences = self.sentences()
                    else:
                        raise ValueError('Enter c to count chars, w to count words, s to count sentences')
            else:
                raise ValueError('You have not chosen any action!')

    def __str__(self):
        """Represents the class objects as a string"""
        return f"Characters: {self.__chars if self.__chars else '-'} \n" \
               f"Words: {self.__words if self.__words else '-'} \n" \
               f"Sentences: {self.__sentences if self.__sentences else '-'}"
