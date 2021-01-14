import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from seaborn import set_style
from imblearn.over_sampling import RandomOverSampler

#create base model
print('Baseline Model:',accuracy_score(y_test, (['>1']*len(y_test))))

#import data
data = pd.read_csv('data/research_data.csv')

#train test split
X_train, X_test, y_train, y_test = train_test_split(list(data.body_text), list(data.one_author),test_size=0.2)

#vectorize body text with 2000 features
vectorizor = TfidfVectorizer(max_features=2500)
X_train_matrix = vectorizor.fit_transform(X_train)
X_test_matrix = vectorizor.fit_transform(X_test)
X_train_matrix = X_train_matrix.todense()
X_test_matrix = X_test_matrix.todense()

#over sampling for class balance before training the data
ros = RandomOverSampler()
X_res, y_res = ros.fit_resample(X_train_matrix, y_train)

#train on random forest
randForest = RandomForestClassifier(class_weight="balanced")
randForest.fit(X_res, y_res)
y_pred = randForest.predict(X_test_matrix)
print('RandomForest:',confusion_matrix(y_test, y_pred), accuracy_score(y_test, y_pred))

#train on gradient boosting
gb = GradientBoostingClassifier().fit(X_res, y_res)
y_pred = gb.predict(X_test_matrix)
print('GradientBoosting:',confusion_matrix(y_test, y_pred), accuracy_score(y_test, y_pred))

#train on naive bayes
nb = MultinomialNB().fit(X_res, y_res)
y_pred = nb.predict(X_test_matrix)
print('Naive Bayes:',confusion_matrix(y_test, y_pred), accuracy_score(y_test, y_pred))

#begin graphing the results on an ROC curve
positive_label = y_test[0]

fprRF, tprRF, thresholds = roc_curve(y_test, randForest.predict_proba(X_test_matrix)[:,1], pos_label = positive_label)
fprGB, tprGB, thresholds = roc_curve(y_test, gb.predict_proba(X_test_matrix)[:,1], pos_label = positive_label)
fprNB, tprNB, thresholds = roc_curve(y_test, nb.predict_proba(X_test_matrix)[:,1], pos_label = positive_label)

roc_aucRF = auc(fprRF, tprRF)
roc_aucGB = auc(fprGB, tprGB)
roc_aucNB = auc(fprNB, tprNB)

plt.figure()
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.title('Classifier ROC Curves One or More Authors')
plt.plot(fprRF, tprRF, color='red', lw=2, label='Random Forest ROC area = %0.2f)' % roc_aucRF)
plt.plot(fprGB, tprGB, color='black', lw=2, label='Gradient Boosting ROC area = %0.2f)' % roc_aucGB)
plt.plot(fprNB, tprNB, color='blue', lw=2, label='Naive Bayes ROC area = %0.2f)' % roc_aucNB)
plt.legend(loc="lower right")
plt.savefig('images/roc_curve_author>1')
plt.show()

#because naive bayes had the highest area under the curve
#I looked at the titles most confidently predicted values for 1 and over 1 authors
highest_pred = nb.predict_proba(X_test_matrix)
#1
data.iloc[pd.Series(highest_pred[:,0]).idxmin()]['title']
#over 1
data.iloc[pd.Series(highest_pred[:,0]).idxmax()]['title']

#show_most_informative_words
def show_most_informative_features(vectorizer, clf, n=20):
    feature_names = vectorizer.get_feature_names()
    coefs_with_fns = sorted(zip(clf.coef_[0], feature_names))
    top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
    print('Top more or\tTop one researcher words')
    for (coef_1, fn_1), (coef_2, fn_2) in top:
        print ("%-15s\t%-15s" % (fn_1, fn_2))

show_most_informative_features(vectorizor, nb, 200)