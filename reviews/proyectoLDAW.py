# -*- coding: utf-8 -*-
"""
LDAW - Project
Gerardo López García A01018739
"""



########## 1. CARGAR ###########
#%% Librerias
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelBinarizer


#%% CSV
df = pd.read_csv('/Users/gLogar/Desktop/juegos_calificados.csv')

#%% DEFINED_FUNCTIONS
 
def binarize_label_columns(df, columns, two_classes_as='single'):
    '''
    Inputs:
        df: Pandas dataframe object.
        columns: Columns to binarize.
        tow_classes_as: How to handle two classes, as 'single' or 'multiple' columns.
    Returns a tuple with the following items:
        df: Pandas dataframe object with new columns.
        binlabel_names: Names of the newly created binary variables.
        lb_objects: a dictionary with columns as keys and sklear.LabelBinarizer
        objects as values.
    '''
    binlabel_names = []
    lb_objects = {}
    for col in columns:
        if len(df[col].unique()) > 1:
            rows_notnull = df[col].notnull() # Use only valid feature observations
            lb = LabelBinarizer()
            binclass = lb.fit_transform(df[col][rows_notnull]) # Fit & transform on valid observations
            if len(lb.classes_) == 2 and two_classes_as == 'multiple':
                binclass = np.hstack((1 - binclass, binclass))
            lb_objects[col] = lb
            if len(lb.classes_) > 2 or two_classes_as == 'multiple':
                col_binlabel_names = [col+'_'+str(c) for c in lb.classes_]
                binlabel_names += col_binlabel_names # Names for the binarized classes
                for n in col_binlabel_names: df[n] = np.NaN # Initialize columns
                df.loc[rows_notnull, col_binlabel_names] = binclass # Merge binarized data
            elif two_classes_as == 'single':
                binlabel_names.append(col+'_bin') # Names for the binarized classes
                df[col+'_bin'] = np.NaN # Initialize columns
                df.loc[rows_notnull, col+'_bin'] = binclass # Merge binarized data
    return df, binlabel_names, lb_objects



########## 6. DATA CLUSTERING ###########
#%%  
df, binlabel_names, lb_objects = binarize_label_columns(df, ['Jugadores', 'ESRB'],two_classes_as='multiple')
df.drop(['Jugadores'], axis=1, inplace=True) 
df.drop(['ESRB'], axis=1, inplace=True)
df.dtypes



########## 8.3 MODEL-LOGISTIC REGRESION ###########
#%% 
from sklearn import tree

df_tree_train =  df.head(15)
df_tree_predict =  df.tail(5)


model3 = tree.DecisionTreeClassifier()
model3.fit(X=df_tree_train[['S1', 'S2', 'S3', 'S4', 'S5','Plataforma','Precio','Jugadores_MMO','Jugadores_Multi','Jugadores_Online','Jugadores_Single','ESRB_E','ESRB_M','ESRB_T']], y=df_tree_train['S6'])
df_tree_predict['S6_predicted'] = model3.predict(df_tree_predict[['S1', 'S2', 'S3', 'S4', 'S5','Plataforma','Precio','Jugadores_MMO','Jugadores_Multi','Jugadores_Online','Jugadores_Single','ESRB_E','ESRB_M','ESRB_T']])
df_tree_predict['error'] = abs(df_tree_predict.S6 - df_tree_predict.S6_predicted) 
print df_tree_predict[['S6', 'S6_predicted', 'error']]
pError = df_tree_predict["error"].mean()
pError
#df_logistic.to_csv('df_logistic.csv', sep=',')
#error promedio  6.46
