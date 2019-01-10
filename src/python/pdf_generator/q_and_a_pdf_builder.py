from data_preparation.q_and_a_html_builder import QAndAHtmlBuilder
from pdf_generator.pdf_builder import PdfBuilder


class QAndAPdfBuilder(PdfBuilder):

    def __init__(self) -> None:
        super().__init__()
        self.html_builder = QAndAHtmlBuilder()

    def _get_html_builder(self):
        return self.html_builder

    def _pdf_report_file(self):
        return 'q-and-a-report.pdf'
