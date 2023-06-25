import string

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


def preprocess_text(text):
    """
    Preprocesses text for sentiment analysis.

    Args:
        text (str): The text to preprocess.

    Returns:
        str: The preprocessed text.
    """

    # Remove punctuation.
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove stop words.
    stop_words = set(stopwords.words("english"))
    text = [word for word in text.split() if word not in stop_words]

    # Stemming.
    stemmer = PorterStemmer()
    text = [stemmer.stem(word) for word in text]

    return " ".join(text)


def predict(model, text):
    # Predict the sentiment
    preprocessed_text = preprocess_text(text)
    print(preprocessed_text)
    prediction, *_ = model.predict([text]).tolist()

    pred_to_label = {0: "negative", 1: "positive"}

    # Make a list of text with sentiment.
    data = {"sentiment": pred_to_label[prediction]}

    return data


if __name__ == "__main__":
    print(
        preprocess_text("I love this product! It's the best thing since sliced bread!")
    )
