#!/usr/bin/env python3

import pytest

from .robot import Questions


@pytest.fixture
def questions():
    q = Questions('data/training_data.json')
    return q


class TestQuestions:
    def test_init(self):
        q = Questions('data/training_data.json')

        assert q.questions_list is not None
        assert len(q.questions_list) == 4
        assert q.questions_detail is not None
        assert len(q.questions_detail.keys()) == 4

    def test_get_next_question_message(self, questions):
        q = questions
        for msg in ["What is your name?", "Are you male or female?", "When were you born?", "Are you a smoker?"]:
            assert q.get_next_question_message() == msg

        assert q.get_next_question_message() is None
        # assert 0

    def test_set_question_answer(self, questions):
        q = questions
        q.get_next_question_message()
        q.set_question_answer('john')

        assert q.current_question['result'] == 'john'

        q.get_next_question_message()
        q.set_question_answer('female')
        assert q.current_question['result'] == 'female'

        q.get_next_question_message()
        q.set_question_answer('2018-01-01')
        assert q.current_question['result'] == '2018-01-01'

        q.get_next_question_message()
        q.set_question_answer('yes')
        assert q.current_question['result'] == 'smoker'

    def test_get_final_answer(self, questions):
        q = questions
        q.get_next_question_message()
        q.set_question_answer('john')
        q.get_next_question_message()
        q.set_question_answer('male')
        q.get_next_question_message()
        q.set_question_answer('2018-01-01')
        q.get_next_question_message()
        q.set_question_answer('no')

        answer = q.get_final_answer()

        assert answer == "john was born in 2018-01-01 and is a male nonsmoker."

    def test_is_valid_result(self):
        q = Questions('data/training_data.json')

        q.get_next_question_message()
        q.set_question_answer('john')

        q.get_next_question_message()
        assert not q.is_valid_result('xxx')
        assert q.is_valid_result('male') is True
        assert q.is_valid_result('female') is True
        assert q.is_valid_result('fexmale') is False

        q.get_next_question_message()

        q.get_next_question_message()
        assert not q.is_valid_result('xxx')
        assert q.is_valid_result('yes') is True
        assert q.is_valid_result('no') is True
        assert q.is_valid_result('i') is False
