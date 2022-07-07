# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:08:49 2022

@author: medadocadmin
"""

import pandas as pd
import sqlite3
db = r'C:\Users\medadocadmin\Documents\NewDovDevelop\sudukoback\db.sqlite3'
dbcon = sqlite3.connect(db)
p  = pd.read_sql_query("SELECT * from django_migrations", dbcon)

puzzleTable = [
    {'puzzleID': 'p1', 
     'sudukoString': '123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890',
     'puzzleName': 'puzzle1', 'difficultyLevel': 'E'},
    
    {'puzzleID': 'p2', 
     'sudukoString': '123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890',
     'puzzleName': 'puzzle2', 'difficultyLevel': 'E'},
    
    ]

puzDF = pd.DataFrame(puzzleTable)
puzDF.to_sql("sudukoapi_puzzle", dbcon, if_exists='append', index=False)
