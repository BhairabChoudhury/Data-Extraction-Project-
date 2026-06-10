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