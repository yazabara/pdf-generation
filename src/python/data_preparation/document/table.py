import pandas as pd


class Table(object):
    """
    Class define working with html data
    """

    def __init__(self, headers) -> None:
        super().__init__()
        # initialize table with header
        self.data_frame = pd.DataFrame(
            columns=headers
        )

    def add_row(self, row):
        """
        Method adds row to existing table
        :param row: dict with header properties
        For example: header is ['First', 'Second'] and available row is: {'First': 1, 'Second': 'value'}
        :return: self
        """
        self.data_frame = self.data_frame.append(
            other=row,
            ignore_index=True
        )
        return self
