import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

data=pd.read_csv('datasets5.csv')
x=data.iloc[:,:-1]
y=data.iloc[:,-1]
x_train,x_test,y_train,y_pred=train_test_split(x,y,test_size=0.25,random_state=42)
clf=MultinomialNB()
clf.fit(x_train,y_train)
y_test=clf.predict(x_test)
print(f"Accuracy :{metrics.accuracy_score(y_pred,y_test)}")
print(f"precision :{metrics.precision_score(y_pred,y_test,average='weighted',zero_division=1)}")
print(f"Accuracy :{metrics.recall_score(y_pred,y_test,average='weighted',zero_division=1)}")