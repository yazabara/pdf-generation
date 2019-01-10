import unittest

from configuration.configuration import configuration
from data_preparation.document.document import Document
from data_preparation.document.list import List
from data_preparation.document.table import Table


class DocumentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        configuration.templates_path = "../../../resources/templates/"

    def test_create_empty_document(self):
        document = Document(None)
        self.assertIsNone(document.title)

        document = Document('Title')
        self.assertIsNotNone(document.title)

    def test_create_document(self):
        html_dic = Document('Title') \
            .add_component('list', List()
                           .add_item('First li element')
                           .add_item('<img alt="test" '
                                     'src="https://cdn.pixabay.com/photo/2015/07/27/19/47/turtle-863336_960_720.jpg" '
                                     'style="height:250px; width:250px" />'
                                     '<p>ij2o<strong>3r92</strong>r092jr 2</p>')
                           ) \
            .add_component('table', Table(['First', 'Second'])
                           .add_row({'First': 1, 'Second': 'value'})
                           .add_row({'First': 2, 'Second': 'new'})
                           .add_row({'First': 3, 'Second': 'new value'})
                           ) \
            .add_component('custom', '<a href="https://github.com/yazabara">yazabara repo</a>') \
            .prepare_html_dict()

        self.assertIsNotNone(html_dic)
        self.assertEqual(3, len(html_dic))


if __name__ == '__main__':
    unittest.main()
