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
    {'puzzleID': 'p5', 
     'sudukoString': '010020300004005060070000008006900070000100002030048000500006040000800106008000000',
     'puzzleName': 'puzzle1', 'difficultyLevel': 'E'},
    
    {'puzzleID': 'p6', 
     'sudukoString': '000123000040050060000000000100000003260070081900000002000000000080060040000294000',
     'puzzleName': 'puzzle2', 'difficultyLevel': 'E'},
    
    ]

puzDF = pd.DataFrame(puzzleTable)
puzDF.to_sql("sudukoapi_puzzle", dbcon, if_exists='append', index=False)
