import logging

from weasyprint import HTML

from data_preparation.data_processor import data_processor
from data_reader.data_reader import data_reader
from src.python.configuration.configuration import configuration
from template_processor.template_processor import template_processor


class PdfGenerator(object):

    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger("PDF Generator")
        self.logger.debug('PDF initialized')

    def generate_sample_report(self):
        file_name = 'report-sample.xlsx'
        self.logger.info('Application generates a PDF report for file {}'.format(file_name))
        data = data_processor.prepare_sample(data_reader.read_exel(file_name))
        result_path = configuration.reports_path + 'report-sample.pdf'

        HTML(
            string=template_processor.prepare_html_sample_data(data)
        ).write_pdf(
            target=result_path,
            stylesheets=[configuration.templates_path + 'report-sample.css']
        )
        self.logger.info('Application finished PDF report generation. Result placed to {}'.format(result_path))


pdf_generator = PdfGenerator()
