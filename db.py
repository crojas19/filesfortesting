import sqlite3
import pandas as pd

#Ubuntu location
con = sqlite3.connect("config\stashtest.sqlite")
#Windows location
#con = sqlite3.connect("StashDBParser\stash-go.sqlite")
df=pd.read_sql_query ("SELECT title,url FROM scenes WHERE created_at >= date('now','-1 day')", con)
cur = con.cursor()

print(df.to_string(index=False))

df.to_csv("config\export_dataframe.csv", index = False, header=True)

#print(df)
#for row in cur.execute('SELECT title,details,url FROM scenes WHERE created_at >= date("now","-1 day"); '):
 #   print(row)


con.close()