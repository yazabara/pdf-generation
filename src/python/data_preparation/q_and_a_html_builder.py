import uuid

from data_preparation.document.document import Document
from data_preparation.html_builder import HtmlBuilder


class QAndAHtmlBuilder(HtmlBuilder):

    def __init__(self) -> None:
        super().__init__()
        self.id = uuid.uuid4()
        self.history = None
        self.questions = []

    def build_document(self):
        document = Document('Report #' + str(self.id))
        document \
            .add_component('question_list', self.questions) \
            .add_component('history', self.history)
        return document

    def html_template_file(self):
        return 'q-and-a-report.html'

    def css_file(self):
        return 'q-and-a-report.css'
