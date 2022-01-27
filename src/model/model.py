import pandas as pds
df = pds.read_csv("mergedTab.csv", encoding='ISO-8859-1', sep=';')
top=[]
df = df.apply (pds.to_numeric, errors='coerce')
df = df.dropna()
print(df)
for i in range(len(df)):
    top.append(df.iloc[i,7])
print(top)
#for i in range(len(top)):

#    if str(top[i])=='nan':
#        top[i]='0'
#top = map(int, top)
#top = list(map(int, top))
top.sort(reverse=True)
T1=top[0]
T2=top[1]
T3=top[2]
T4=top[3]
T5=top[4]
print(str(T5))
print(str(round(df.iloc[38218,7])))


for i in range(len(df)):
    if str(round(df.iloc[i,7]))==str(T5):
        print(df.iloc[i,0]) 


def ComputeMean():
    mean = 0
    return (mean)

def ComputeMedian:
    median = 0
    return (median)    
    
    
