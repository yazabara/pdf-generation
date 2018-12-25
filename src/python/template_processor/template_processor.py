import logging

from jinja2 import Environment, FileSystemLoader

from configuration.configuration import configuration


class TemplateProcessor(object):
    """
    Template processor prepares HTML data for some pre-processed data
    """

    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger("Template Processor")
        self.logger.debug('Template Processor initialized')
        self.template_env = Environment(loader=FileSystemLoader(configuration.templates_path))

    def prepare_html_sample_data(self, data):
        self.logger.info('Application prepares html data')
        template = self.template_env.get_template('report-sample.html')
        template_vars = {
            "title": "Sales Funnel Report - National",
            "national_pivot_table": data.to_html()
        }
        return template.render(template_vars)


template_processor = TemplateProcessor()
