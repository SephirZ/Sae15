# importing des modules
import pandas as pd
import glob
import os

# detection des fichiers
joined_files = os.path.join('U:\Documents\TESTCSV', "youtube*.csv")

# une liste des fichiers est créer.
joined_list = glob.glob(joined_files)

# Les fichiers sont fusionnés
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
print(df)
export_csv = df.to_csv ('Donnees.csv', index=None, header=True, encoding='utf-8', sep=',')
