import pandas as pd

from data_preparation.document.doc_component import DocComponent


class Table(DocComponent):
    """
    Class contains table data for document (html/doc)
    """

    def __init__(self, headers) -> None:
        super().__init__()
        # initialize table with header
        self.data = pd.DataFrame(
            columns=headers
        )
        self.logger.info('Table {} has headers: {}'.format(self.id, headers))

    def component_type(self):
        return 'Table'

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
