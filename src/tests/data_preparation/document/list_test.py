import unittest

from data_preparation.document.list import List


class TableTest(unittest.TestCase):

    def test_table_not_none(self):
        array = List()
        self.assertIsNotNone(array.data)

    def test_add_row_works_correct(self):
        array = List()
        self.assertIsNotNone(array.data)
        self.assertEqual(0, len(array.data.index))
        array \
            .add_item(1) \
            .add_item(2)
        self.assertEqual(2, len(array.data.index))
        array \
            .add_item('Some data') \
            .add_item('Data with link: https://github.com/yazabara')
        self.assertEqual(4, len(array.data.index))


if __name__ == '__main__':
    unittest.main()
