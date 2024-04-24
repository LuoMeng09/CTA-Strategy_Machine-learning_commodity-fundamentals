import sklearn
import numpy as np
import pandas as pd
from data_processor import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV



score_knn_equity = pd.DataFrame()
param_grid_knn=[
    {
        'weights': ['distance'],
        'n_neighbors': [i for i in range(2, 31)],
        'p':[i for i in range(1, 6)],
        'leaf_size':[i for i in range(200,1005,10)]
    }
]

def KNN_param_select(x_train,y_train):
    score_knn = pd.DataFrame()
    grid_search=GridSearchCV(estimator=KNeighborsClassifier(),param_grid=param_grid_knn,cv=5,verbose=2)   
    grid_search.fit(x_train,y_train)
    score_knn.loc['best_estimator'] = grid_search.best_estimator_
    score_knn.loc['best_score_'] = grid_search.best_score_
    score_knn.loc['best_index_'] = grid_search.best_index_
    return score_knn


def KNeighbors(x_train,x_test,y_train,y_test,X,n,step,p,term,p1,p2,price_name):
    knn = KNeighborsClassifier(n_neighbors=n,algorithm='auto',leaf_size=step,p=p).fit(x_train,y_train)
    knn_pred_train_prob = knn.predict_proba(x_train)
    knn_pred_test_prob = knn.predict_proba(x_test)
    knn_pred_train = pd.DataFrame(knn_pred_train_prob[:,1])[0].apply(lambda x: ComparePercent(p1,p2,x))
    knn_pred_test = pd.DataFrame(knn_pred_test_prob[:,1])[0].apply(lambda x: ComparePercent(p1,p2,x))
    return  knn_pred_train,knn_pred_test,knn_pred_train_prob,knn_pred_test_prob
