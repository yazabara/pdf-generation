import logging

import pandas as pd

from src.python.configuration.configuration import configuration


class DataReader(object):
    """
    Date Reader reads information from several storages (exel,json,...etc)
    """

    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger("Data Reader")
        self.logger.debug('Data Reader initialized')

    def read_exel(self, file_name):
        file_path = configuration.data_path + file_name
        self.logger.info('Application reads data from file: {}'.format(file_path))
        return pd.read_excel(file_path)


data_reader = DataReader()
