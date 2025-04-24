from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_classifier(data):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data['masked_email'])
    y = data['category']
    clf = RandomForestClassifier()
    clf.fit(X, y)
    joblib.dump(clf, 'classifier_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')
