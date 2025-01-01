import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

msg = pd.read_csv('document.csv', names=['message', 'label'])
msg['labelnum'] = msg.label.map({'pos': 1, 'neg': 0})

X, y = msg['message'], msg['labelnum']
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)

count_v = CountVectorizer()
Xtrain_dm = count_v.fit_transform(Xtrain)
Xtest_dm = count_v.transform(Xtest)

clf = MultinomialNB()
clf.fit(Xtrain_dm, ytrain)
pred = clf.predict(Xtest_dm)

for doc, p in zip(Xtrain, pred):
    p = 'pos' if p == 1 else 'neg'
    print("%s -> %s" % (doc, p))

print(f"\nAccuracy: {accuracy_score(ytest, pred)}")
print(f"Recall: {recall_score(ytest, pred)}")
print(f"Precision: {precision_score(ytest, pred)}")
print(f"Confusion Matrix: \n{confusion_matrix(ytest, pred)}")
