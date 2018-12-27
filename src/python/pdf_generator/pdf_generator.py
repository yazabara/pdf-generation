import logging

from weasyprint import HTML

from data_preparation.data_processor import data_processor
from data_preparation.document.document import Document
from data_preparation.document.list import List
from data_preparation.document.table import Table
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

    def generate_custom_report(self):
        result_path = configuration.reports_path + 'report-custom.pdf'
        doc = Document(None)
        list_data = List() \
            .add_item('First li element') \
            .add_item('Second li element') \
            .add_item('Second li element') \
            .add_item('<img alt="test" '
                      'src="https://cdn.pixabay.com/photo/2015/07/27/19/47/turtle-863336_960_720.jpg" '
                      'style="height:250px; width:250px" />'
                      '<p>ij2o<strong>3r92</strong>r092jr 2</p>')

        table_data = Table(['First', 'Second']) \
            .add_row({'First': 1, 'Second': 'value'}) \
            .add_row({'First': 2, 'Second': 'new'}) \
            .add_row({'First': 3, 'Second': 'new value'})

        doc.add_component('custom_list', list_data)
        doc.add_component('custom_table', table_data)
        doc.add_component('custom_component', '<a href="https://github.com/yazabara">yazabara repo</a>')

        HTML(
            string=template_processor.prepare_html_custom_data(doc.prepare_html_dic())
        ).write_pdf(
            target=result_path,
            stylesheets=[configuration.templates_path + 'custom-report.css']
        )
        self.logger.info('Application finished PDF report generation. Result placed to {}'.format(result_path))


pdf_generator = PdfGenerator()
