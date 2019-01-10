import pandas as pd

from data_preparation.document.doc_component import DocComponent


class Question(DocComponent):
    """
    Class contains question data for document (html/doc)
    """

    def __init__(self, question_title) -> None:
        super().__init__()
        self.question_title = question_title
        self.question_content = None
        self.sub_questions = None
        self.logger.info('Question {} created with title: {}'.format(self.id, question_title))

    def add_question_content(self, question_content):
        self.question_content = question_content
        return self

    def add_sub_question(self, title, content):
        if self.sub_questions is None:
            self.sub_questions = pd.Series({})

        self.sub_questions = self.sub_questions.append(
            to_append=pd.Series([{
                'title': title,
                'content': content
            }]),
            ignore_index=True
        )
        self.logger.info('Subquestion {} added to question {}'.format(title, self.id))
        return self

    def component_type(self):
        return 'Question'

    def convert_to_html(self):
        template = self.template_env.get_template('question.html')
        template_vars = {
            "question_title": self.question_title,
            "question_content": self.question_content,
            "sub_questions": self.sub_questions
        }
        return template.render(template_vars)
