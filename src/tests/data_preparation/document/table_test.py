import unittest

from data_preparation.document.table import Table


class TableTest(unittest.TestCase):

    def test_table_not_none(self):
        t = Table(None)
        self.assertIsNotNone(t.data)
        t = Table([])
        self.assertIsNotNone(t.data)
        t = Table(['First column', 'Second column', 'Third column'])
        self.assertIsNotNone(t.data)

    def test_add_row_works_correct(self):
        t = Table(['First', 'Second']) \
            .add_row({'First': 1, 'Second': 'value'})
        self.assertIsNotNone(t.data)
        self.assertEqual(1, len(t.data.index))
        t.add_row({'First': 2, 'Second': 'new'}) \
            .add_row({'First': 3, 'Second': 'new value'})
        self.assertEqual(3, len(t.data.index))


if __name__ == '__main__':
    unittest.main()
