import pandas as pd

dataset = pd.read_csv("C:/Users/Karan Kalla/Desktop/Datasets/Heart_processed_og.csv")

X = dataset.iloc[:, 0:10].values
y = dataset.iloc[:, 10].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20, random_state=3)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

from sklearn.model_selection import cross_val_score
scores = cross_val_score(classifier, X, y, cv=5)

print(scores.mean())

