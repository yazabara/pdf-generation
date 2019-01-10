import logging
import uuid
from abc import ABCMeta, abstractmethod

from jinja2 import Environment, FileSystemLoader

from configuration.configuration import configuration


class HtmlBuilder(metaclass=ABCMeta):

    def __init__(self) -> None:
        super().__init__()
        self.id = uuid.uuid4()
        self.logger = logging.getLogger('Html Builder')
        self.logger.debug('Html Builder {} was initialized'.format(self.id))
        self.template_env = Environment(loader=FileSystemLoader(configuration.templates_path))

    def render_html_with_data(self):
        """
        Method loads and render html template with data
        :return: html rendered data
        """
        self.logger.info('Builder {} prepares html data for {} file'.format(self.id, self.html_template_file()))
        return self \
            .template_env.get_template(self.html_template_file()) \
            .render(self.build_document().prepare_html_dict())

    @abstractmethod
    def build_document(self):
        """
        Methods build document model for report generation
        :return: document model
        """
        pass

    @abstractmethod
    def html_template_file(self):
        """
        Method returns html template filename for report generation
        :return: html template name
        """
        pass

    @abstractmethod
    def css_file(self):
        """
        Method returns css file for report generation
        :return: css file name
        """
        pass
