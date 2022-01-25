# importing libraries
import pandas as pd
import glob
import os

# merging the files
joined_files = os.path.join('U:\Documents\TESTCSV', "youtube*.csv")

# A list of all joined files is returned
joined_list = glob.glob(joined_files)

# Finally, the files are joined
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
print(df)
export_csv = df.to_csv ('Donnees.csv', index=None, header=True, encoding='utf-8', sep=',')