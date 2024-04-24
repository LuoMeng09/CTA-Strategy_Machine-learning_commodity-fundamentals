import sklearn
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression as LR 
from sklearn import preprocessing
from data_processor import *


param_grid_l1=[
    {
        'penalty': ['l1'],
        'solver':['liblinear','lbfgs','newton-cg','sag','saga'],
        'C': [i for i in np.arange(0.1,10.1,0.1)],
        'max_iter':[i for i in range(200,1005,10)]

    }
]

def Logistic_Lasso_param_select(x_train,y_train,param_grid_l1):
    score_l1 = pd.DataFrame()
    lrl1 = LR()
    grid_search = GridSearchCV(lrl1,param_grid_l1,cv=5,verbose=2)
    grid_search.fit(x_train,y_train)
    score_l1.loc['best_estimator'] = grid_search.best_estimator_
    score_l1.loc['best_score_'] = grid_search.best_score_
    score_l1.loc['best_index_'] = grid_search.best_index_
    return score_l1


def Logistic_Lasso(xtrain,xtest,ytrain,ytest,X,c,method,price_name,p1,p2):
    '''
    penalty: The selectable values are "l1" and "l2", corresponding to L1 regularization and L2 regularization, respectively. The default is L2 regularization.
    solver: Determines the optimization method for the logistic regression loss function. There are four algorithms to choose from: liblinear, lbfgs, newton-cg, sag.
    C: The inverse of the regularization strength, which must be a positive floating-point number. If not specified, the default is 1.0, which means the default regularization term is one. The smaller the value of C, the heavier the penalty on the loss function, the stronger the effect of regularization, and the parameters θ will gradually be compressed to become smaller and smaller.
    '''
    lrl1 = LR(penalty='l1',  C=c, solver = method,random_state=1234).fit(xtrain,ytrain.loc[:,price_name])
    xcoef = lrl1.coef_[0]    
    l1_train_prob = lrl1.predict_proba(xtrain)
    l1_test_prob = lrl1.predict_proba(xtest)
    l1_pred_train = pd.DataFrame(l1_train_prob[:,1])[0].apply(lambda x: ComparePercent(p1,p2,x))
    l1_pred_test = pd.DataFrame(l1_test_prob[:,1])[0].apply(lambda x: ComparePercent(p1,p2,x))
    return  l1_pred_train,l1_pred_test,xcoef,l1_train_prob,l1_test_prob

