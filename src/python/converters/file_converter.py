from abc import abstractmethod


class FileConverter(object):

    @abstractmethod
    def convert(self,  input_file, output_file):
        pass
