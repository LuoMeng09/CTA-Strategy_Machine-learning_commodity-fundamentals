import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV


param_grid_rf=[
    {
        'n_estimators': [i for i in range(200,810,10)],
        'min_samples_split': [i for i in np.arange(0.3,0.72,0.02)],
        'max_depth':[5]                        
    }
]

def RandomForest_param_select(x_train,y_train,param_grid_rf):
    score_rf = pd.DataFrame()
    rf=RandomForestClassifier(random_state=1234)
    rf_grid_search =GridSearchCV(rf,param_grid=param_grid_rf,cv=5,verbose=2)   
    rf_grid_search.fit(x_train,y_train)
    score_rf.loc['best_estimator'] = str(rf_grid_search.best_estimator_)
    score_rf.loc['best_score'] =  rf_grid_search.best_score_
    score_rf.loc['best_index'] =  rf_grid_search.best_index_
    return score_rf


def RandomForest(x_train,x_test,y_train,y_test,X,n,split,depth,price_name):
    rf = RandomForestClassifier(n_estimators=n,min_samples_split=split,random_state=1234,max_depth=depth).fit(x_train,y_train)
    rf_pred_train = rf.predict(x_train)
    rf_pred_test = rf.predict(x_test)
    rf_pred_all = rf.predict(X)
    return  rf_pred_train,rf_pred_test, rf_pred_all
