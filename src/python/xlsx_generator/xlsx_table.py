import logging
import uuid

import pandas as pd


class XlsxTable:

    def __init__(self, headers) -> None:
        self.id = uuid.uuid4()
        # initialize table with header
        self.data = pd.DataFrame(
            columns=headers
        )
        self.logger = logging.getLogger("Component.XlsxTable")
        self.logger.info('Table {} created with headers: {}'.format(self.id, headers))

    def add_row(self, row):
        """
        Method adds row to existing table
        :param row: dict with header properties
        For example: header is ['First', 'Second'] and available row is: {'First': 1, 'Second': 'value'}
        :return: self
        """
        self.data = self.data.append(
            other=row,
            ignore_index=True
        )
        self.logger.info('Row {} added to table {}'.format(self.id, row))
        return self
