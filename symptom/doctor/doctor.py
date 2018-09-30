from doctor.identifier import NBSymptomIdentifier
from doctor.transformer import Transformer


class Doctor:
    def __init__(self, name):
        self.name = name
        self.transformer = Transformer()
        self.identifier = NBSymptomIdentifier()

    def talk(self):
        """read the description for the feeling and symptom
        """
        while True:
            try:
                raw_data = input("Input your symptom description:")

                # print("You input:", raw_data)

                data = self.transformer(raw_data)

                # print("final data: ", data)

                symptom = self.analyze(data)
                print("Available symptom :", symptom)
                print("")
            except KeyboardInterrupt:
                break

        print("\n\n******See you next time******\n")

    def analyze(self, data, output_file=None):
        """Output the symptoms
        """
        symptom = self.identifier(data)
        return symptom
