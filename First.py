import numpy as np
import pandas as pd

df = pd.read_csv(r'anime.csv')

# Extract text between ( and )
def extract_episodes(txt):
    check = False
    data = ""

    for ch in str(txt):
        if ch == "(":
            check = True
            continue

        if ch == ")":
            return data

        if check:
            data += ch

    return data

df["Episodes"] = df["Title"].apply(extract_episodes)

print(df[["Title", "Episodes"]].head())

df['Episodes'] = df['Episodes'].str.replace(' eps', '')# remove eps from the column  

df['Episodes'] = df['Episodes'].astype(float) # change object into float  
print(df[["Title", "Episodes"]].head()) ; 

print(df['Episodes'].dtype)  


#  now  abtraction of time from title 

def extract_time(txt):
    cheak = False ; 
    data = "" ; 
    for i in range(len(txt)):
        if txt[i] ==")": 
            for j in range(i+1,i+20):
                data+=txt[j] 

            return data 



df['Total Time'] = df['Title'].apply(extract_time)

print(df[['Title','Total Time']].head())

