import pandas as pd

from data_preparation.document.doc_component import DocComponent


class List(DocComponent):
    """
    Cass contains list data for document (html/doc)
    """

    def __init__(self) -> None:
        super().__init__()
        self.data = pd.Series({})

    def component_type(self):
        return 'List'

    def add_item(self, item):
        self.data = self.data.append(
            to_append=pd.Series([item]),
            ignore_index=True
        )
        self.logger.info('Item {} added to list {}'.format(self.id, item))
        return self

    def convert_to_html(self):
        template = self.template_env.get_template('list.html')
        template_vars = {
            "data": self.data
        }
        return template.render(template_vars)
