from nltk.stem import PorterStemmer
from textblob import TextBlob


class Transformer:
    """
    Process the data including:
        - lower words
        - correct words
        - stem words
    """

    def __init__(self):
        self.st = PorterStemmer()

    def __call__(self, raw_data: str):
        """Transform the raw_data to a new data
        """
        word_list = []

        # corrrect the words
        t = TextBlob(raw_data).correct()

        # t.tokenize()
        # for w in t.tokenize():
        #     w = self.st.stem(w.lower())
        #     word_list.append(w)

        word_list = [self.st.stem(w.lower()) for w in t.tokenize()]

        s = " ".join(word_list)
        tb = TextBlob(s).correct()

        return str(tb)
