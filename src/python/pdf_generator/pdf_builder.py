import logging
import uuid
from abc import abstractmethod, ABCMeta

from weasyprint import HTML

from configuration.configuration import configuration


class PdfBuilder(metaclass=ABCMeta):

    def __init__(self) -> None:
        super().__init__()
        self.id = uuid.uuid4()
        self.logger = logging.getLogger('PDF Builder')
        self.logger.debug('PDF Builder {} was initialized'.format(self.id))

    def build_pdf(self):
        """
        Method generates PDF using html builder
        """
        self.logger.info('PDF Builder {} starts to generate report for {}'.format(self.id, self._pdf_report_file()))
        html_builder = self._get_html_builder()
        result_path = configuration.reports_path + self._pdf_report_file()
        HTML(
            string=html_builder.render_html_with_data()
        ).write_pdf(
            target=result_path,
            stylesheets=[configuration.templates_path + html_builder.css_file()]
        )
        self.logger.info('PDF Builder {} finished report generation. Result placed to {}'.format(self.id, result_path))

    @abstractmethod
    def _get_html_builder(self):
        """
        Method return html document builder
        :return: html builder
        """
        pass

    @abstractmethod
    def _pdf_report_file(self):
        """
        Method returns pdf file name for reports result
        :return: report name
        """
        pass
