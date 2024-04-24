import sklearn
import numpy as np
import pandas as pd
from data_processor import *
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeRegressor,DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

base_unit = [DecisionTreeClassifier(max_depth=1,random_state=1234),
        DecisionTreeClassifier(max_depth=2,random_state=1234),
        DecisionTreeClassifier(max_depth=3,random_state=1234),
        DecisionTreeClassifier(max_depth=4,random_state=1234),
        DecisionTreeClassifier(max_depth=5,random_state=1234)]

param_grid_ada=[
    {
        'n_estimators': [i for i in range(200,1005,10)],
        'learning_rate': [i for i in np.arange(0.01,1.01,0.01)]
        'base_estimator':[i for i in base_unit]
                                
    }
]
def AdaBoost_param_select(x_train,y_train):
    score_ada = pd.DataFrame()
    ada=AdaBoostClassifier(base_estimator=base_unit,random_state=1234)
    grid_search=GridSearchCV(ada,param_grid=param_grid_ada,cv=5,verbose=2)   
    grid_search.fit(x_train,y_train)
    score_ada.loc['best_estimator'] = grid_search.best_estimator_
    score_ada.loc['best_score'] = grid_search.best_score_
    score_ada.loc['best_index'] = grid_search.best_index_
    return score_ada



