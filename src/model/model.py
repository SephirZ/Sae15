import pandas as pds
df = pds.read_csv("mergedTab.csv", encoding='ISO-8859-1', sep=';')
top=[]
df['views'] = df['views'].fillna(0)
df = df.drop_duplicates(subset=['video_id'], keep='last')
for i in range(len(df)):
    top.append(df.iloc[i,7])
for i in range(len(top)):
    if str(top[i])=='nan':
       top[i]='0'
top = map(int, top)
top = list(map(int, top))
top.sort(reverse=True)
T1=top[0]
T2=top[1]
T3=top[2]
T4=top[3]
T5=top[4]
for i in range(len(df)):
    if round(df.iloc[i,7])==(T5):
        print('TOP 5 : {} avec un total de {} vues ! '.format(df.iloc[i,2],round(df.iloc[i,7])))

for i in range(len(df)):
    if round(df.iloc[i,7])==(T4):
        print('TOP 4 : {} avec un total de {} vues ! '.format(df.iloc[i,2],round(df.iloc[i,7])))

for i in range(len(df)):
    if round(df.iloc[i,7])==(T3):
        print('TOP 3 : {} avec un total de {} vues ! '.format(df.iloc[i,2],round(df.iloc[i,7])))

for i in range(len(df)):
    if round(df.iloc[i,7])==(T2):
        print('TOP 2 : {} avec un total de {} vues ! '.format(df.iloc[i,2],round(df.iloc[i,7])))

for i in range(len(df)):
    if round(df.iloc[i,7])==(T1):
        print('TOP 1 : {} avec un total de {} vues ! '.format(df.iloc[i,2],round(df.iloc[i,7])))

def ComputeMean(df):
    mean = 0
    z=0
    sommeT = 0
    df['likes'] = df['likes'].fillna(0)
    for i in range(len(df)):
        if df.iloc[i,8]==0:
            z+=1
    df = df.drop_duplicates(subset=['video_id'], keep='last')
    for i in range(len(df)):
        mean+=df.iloc[i,8]
    sommeT=len(df)-z
    print('Toutes les vidéos réunies cumulent une moyenne de {} likes.'.format(round(mean/sommeT)))
    return (mean)
ComputeMean(df)


def ComputeMedian(df):
    median = 0
    z = 0
    sommeT = 0
    df['dislikes'] = df['dislikes'].fillna(0)
    for i in range(len(df)):
        if df.iloc[i, 9] == 0:
            z += 1
    df = df.drop_duplicates(subset=['video_id'], keep='last')
    for i in range(len(df)):
        median += df.iloc[i, 9]
    sommeT = len(df) - z
    print('Toutes les vidéos réunies cumulent une moyenne de {} dislikes.'.format(round(median/sommeT)))
    return (median)
ComputeMedian(df)

    
