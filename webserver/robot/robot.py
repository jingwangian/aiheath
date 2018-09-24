import time
import random
import json
import os


class ChatRobot:
    def __init__(self, name, file_name=None, **kwargs):
        self.name = name
        self.responses = {
            "how are you today?": ["I am fine.Thank you.", "I am good.", "Good, how about you?"],
            "what's your name?": ["my name is {0}".format(name)],
            "what's today's weather?": ["the weather is {0}".format('sunny')],
            "default": ["default message"]
        }
        self.last_message = ''
        self.last_response = ''

        if file_name is None:
            file_name = os.path.join(os.getcwd(), 'robot/data/training_data.json')
        self.train(file_name)

    def print_response(self):
        print(self.responses)

    def start(self):
        print(self.responses['start'])
        while True:
            msg = input("User Input:")
            self.send_message(msg)
            print('')

    # def input_message_by_console(self):

    def send_message(self, message):
        message = message.lower()
        time.sleep(0.5)

        res = self.get_response(message)

        print("Doctor: " + res)

    def get_response(self, message):
        message = message.lower()
        self.last_message = message
        if message in self.responses:
            self.last_response = self.responses[message]
            return self.last_response
        elif self.last_response == 'How many days did you got this Headache?':
            try:
                n = int(message)
                self.last_response = ''
                return "So you got Headache for {} days. You should go to see the doctor!".format(n)
            except ValueError:
                return "Please input a valid number!"
        else:
            res = "Sorry I can't understand what you said. Can you say again?"  # + self.last_response
            return res

    def match_rule(rules, message):
        pass

    def train(self, file_name):
        """Train new conversation
        """
        with open(file_name) as fp:
            self.responses = json.load(fp)
