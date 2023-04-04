import pandas as pd
dataset = pd.read_csv("C:/Users/Karan Kalla/Desktop/Datasets/Heart_processed_og.csv")
X = dataset.iloc[:, 0:10].values
y = dataset.iloc[:, 10].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(svclassifier, X, y, cv=5)

print(cv_scores)

print(cv_scores.mean())