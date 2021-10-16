# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 19:23:32 2021

@author: James Ang
"""

import re
import pandas as pd

def topStudents(df):
    # Write your code here
    
    
    df = df[df.isnull().sum(axis=1) < 2]
    
    medians = df.median()
    
    for col in df.columns[1:]:
        df.loc[:,col] = df.loc[:,col].fillna(medians[col]).copy()
        
    for i, names in enumerate(df['student_id']):
        #print(i)
        #print(names)
        # df['student_id'][i] = re.sub('[^0-9]','', df['student_id'][i])
        # a = 
        df.loc[i,'student_id'] = re.sub('[^0-9]','', df.loc[i,'student_id'])
        # .loc[row_indexer,col_indexer]
    df["weighted"] = 0.5*df["math_score"] + 0.2*df['reading_score'] + 0.3*df['writing_score']
    
    df = df[df["weighted"]>70]
    
    df = df.sort_values(by=['weighted'], ascending=False)
    
    final = df[['student_id']]
    
    return final

if __name__ == '__main__':
    
    
    df = pd.read_csv('test.csv')
    
    ratings = topStudents(df)
    print(ratings)