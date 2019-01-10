import logging

from pdf_generator.q_and_a_pdf_builder import QAndAPdfBuilder


class PdfGenerator(object):

    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger("PDF Generator")
        self.logger.debug('PDF Generator initialized')

    def build_q_and_a_report(self):
        self.logger.info("PDF generation Q&A report started")
        QAndAPdfBuilder().build_pdf()
        self.logger.info("PDF generation Q&A report finished")


pdf_generator = PdfGenerator()
