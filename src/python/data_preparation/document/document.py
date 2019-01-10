from data_preparation.document.doc_component import DocComponent


class Document(object):
    """
    Class defines working with document.
    """

    def __init__(self, title) -> None:
        super().__init__()
        self.title = title
        self.__data = {}

    def add_component(self, key, component):
        """
        Method adds component to document
        :param key: component key
        :param component: component data
        :return: self
        """
        self.__data[key] = component
        return self

    def prepare_html_dict(self):
        """
        Method converts all data to html blocks
        :return: dict with html parsed blocks
        """
        dictionary = {k: Document.__convert_component_to_html(v) for k, v in self.__data.items()}
        dictionary['title'] = self.title
        return dictionary

    @staticmethod
    def __convert_component_to_html(component):
        if component is None:
            return ''
        # component
        if isinstance(component, DocComponent):
            return component.convert_to_html()
        # array of objects
        if isinstance(component, list):
            return [Document.__convert_component_to_html(element) for element in component]
        # some value
        return component
