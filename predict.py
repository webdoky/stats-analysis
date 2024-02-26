import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression

from url_to_text import url_to_text

vectorizer = TfidfVectorizer()

def create_ctr_model(stats: pd.DataFrame) -> LinearRegression:
    # create a vectorizer
    # create a model
    model = LinearRegression()
    texts = stats["Text"]
    tfidf = vectorizer.fit_transform(texts)
    model.fit(tfidf, stats["Clicks"])
    return model
    
def predict_ctr(model: LinearRegression, registry: dict, url: str) -> float:
    # convert url to text
    text = url_to_text(registry, url)
    # convert text to vector
    vector = vectorizer.transform([text])
    # predict ctr
    return model.predict(vector)[0]
