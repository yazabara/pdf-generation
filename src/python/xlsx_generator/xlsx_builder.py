import xlsxwriter

from xlsx_generator.xlsx_table import XlsxTable


class XlsxBuilder:
    """
    https://xlsxwriter.readthedocs.io/example_django_simple.html
    https://xlsxwriter.readthedocs.io/example_autofilter.html
    """

    def __init__(self, table: XlsxTable) -> None:
        super().__init__()
        self.table = table
        self.workbook = xlsxwriter.Workbook('hello.xlsx')

    def generate(self):
        self.workbook.add_worksheet()
        self.__prepare_headers()
        self.__populate_data()
        self.workbook.close()

    def __populate_data(self):
        for worksheet in (self.workbook.worksheets()):
            row = 1
            for row_data in (self.table.data.values.tolist()):
                worksheet.write_row(row, 0, row_data)
                row += 1

    def __prepare_headers(self):
        bold = self.workbook.add_format({'bold': 1})
        headers = list(self.table.data.columns.values)
        # Set up several sheets with the same data.
        for worksheet in (self.workbook.worksheets()):
            # Make the columns wider.
            worksheet.set_column('A:D', 12)
            # Make the header row larger.
            worksheet.set_row(0, 20, bold)
            # Make the headers bold.
            worksheet.write_row('A1', headers)
