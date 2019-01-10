import unittest

from data_preparation.document.question import Question


class QuestionTest(unittest.TestCase):

    def test_question_none_conditions(self):
        t = Question(None)
        self.assertIsNone(t.question_title)
        self.assertIsNone(t.question_content)
        self.assertIsNone(t.sub_questions)
