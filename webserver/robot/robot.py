import time
import json
import os


class ChatRobot:
    def __init__(self, name, file_name=None, **kwargs):
        self.name = name
        self.questions = []

        if file_name is None:
            file_name = os.path.join(os.getcwd(), 'robot/data/training_data.json')
        self.file_name = file_name
        self.chat_finished = False
        self.train(file_name)

    def reset(self):
        self.chat_finished = False
        self.questions = Questions(self.file_name)

    def start(self):
        """Used in concole
        """
        for i in self.questions.questions_list:
            print("Doctor: " + self.questions.get_next_question_message())
            msg = input("User Input:")
            while not self.questions.set_question_answer(msg):
                print("Invalid Input: {}".format(self.questions.get_expected_prompt_message()))
                msg = input("User Input:")
                print('')

            print('')

        print(self.questions.get_final_answer())

    def send_message(self, message):
        message = message.lower()
        time.sleep(0.5)

        res = self.get_response(message)

        print("Doctor: " + res)

    def get_first_question(self):
        return self.questions.get_next_question_message()

    def get_response(self, message):
        if self.questions.is_valid_result(message):
            self.questions.set_question_answer(message)
        else:
            msg = self.questions.get_expected_prompt_message()
            return "Invalid input, please input : {}".format(msg)

        try:
            msg = self.questions.get_next_question_message()
            return msg
        except StopIteration:
            return None

    def get_final_answer(self):
        self.chat_finished = True
        return self.questions.get_final_answer()

    def train(self, file_name):
        """Train new conversation
        """
        self.questions = Questions(file_name)


class Questions:
    def __init__(self, file_name):
        self.index = 0
        self.file_name = file_name
        self.questions_list = []
        self.questions_detail = {}

        self.load(file_name)
        self.msg = self.message_generator()

    def get_expected_prompt_message(self):
        expected = self.current_question['expected']
        if len(expected) > 0:
            return '/'.join(expected)
        else:
            return ''

    def message_generator(self):
        for key in self.questions_list:
            self.current_question = self.questions_detail[key]
            print("next message:", self.current_question['message'])
            yield self.current_question['message']

    def get_next_question_message(self):
        try:
            q_msg = next(self.msg)
        except StopIteration:
            return None

        return q_msg

        # self.index += 1
        # try:
        #     key = self.questions_list[self.index - 1]
        # except IndexError:
        #     return None

        # self.current_question = self.questions_detail[key]
        # print("next message:", self.current_question['message'])
        # return self.current_question['message']

    def set_question_answer(self, message):
        if not self.is_valid_result(message):
            return False

        expected = self.current_question['expected']
        if expected:
            self.current_question['result'] = expected[message]
        else:
            self.current_question['result'] = message

        return True

    def is_valid_result(self, message) -> bool:
        """Check the input message is valid or not
        """
        if len(message) == 0:
            return False

        expected = self.current_question['expected']
        if expected:
            if message in expected:
                return True
            else:
                return False
        else:
            return True

    def get_final_answer(self) -> str:
        answer = "{} was born in {} and is a {} {}.".format(self.questions_detail['username']['result'],
                                                            self.questions_detail['birth_date']['result'],
                                                            self.questions_detail['gender']['result'],
                                                            self.questions_detail['smoker']['result'])

        return answer

    def load(self, file_name):
        with open(file_name) as fp:
            d = json.load(fp)

            self.questions_list = d["questions_list"]
            self.questions_detail = d["questions_detail"]
