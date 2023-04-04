import pandas as pd
dataset = pd.read_csv("C:/Users/Karan Kalla/Desktop/Datasets/dicot_processed.csv")
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

######################################################

X_train_rf, X_test_rf, y_train_rf, y_test_rf = train_test_split(X, y, test_size=0.3, random_state=3)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20, random_state=3)
classifier.fit(X_train_rf, y_train_rf)
y_pred_rf = classifier.predict(X_test_rf)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test_rf,y_pred_rf))
print(classification_report(y_test_rf,y_pred_rf))
print(accuracy_score(y_test_rf, y_pred_rf))


################################
# plot


from sklearn.metrics import roc_curve, auc
fpr, tpr, thresholds = roc_curve(y_test, y_pred)
fpr_rf, tpr_rf, thresholds_rf = roc_curve(y_test_rf, y_pred_rf)
roc_auc = auc(fpr, tpr)
roc_auc_rf = auc(fpr_rf, tpr_rf)
import matplotlib.pyplot as plt

plt.figure()
plt.plot(fpr, tpr, color='orange', lw=2, label='ROC curve for SVM(AUC = %0.2f)' % roc_auc)
plt.plot(fpr_rf, tpr_rf, color='green', lw=2, label='ROC curve for RF (AUC = %0.2f)' % roc_auc_rf)
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()