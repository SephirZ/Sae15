import pandas as pds
lettre=['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']
catID=['2','1','10','15','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44']
def pourcentage(x):
    pourc=x*100/46732
    return pourc
df = pds.read_csv("mergedTab.csv", encoding='ISO-8859-1', sep=';')
aber=0
miss=0
corr=0
print(len(df))
for i in range (len(df)):
    if str(df.iloc[i,0])=='nan':
        miss+=1
    elif len(str(df.iloc[i, 0])) != 11:
        aber += 1
    elif str(df.iloc[i, 1]) == 'nan':
        miss += 1
    elif len(str(df.iloc[i, 1])) != 8:
        aber += 1
    elif any(x in df.iloc[i, 1] for x in lettre):
        aber += 1
    elif str(df.iloc[i,2])=='nan':
        miss+=1
    elif str(df.iloc[i,3])=='nan':
        miss+=1
    elif str(df.iloc[i,4])=='nan':
        miss+=1
    elif not any(x in str(df.iloc[i,4]) for x in catID):
        aber+=1
    elif str(df.iloc[i,5])=='nan':
        miss+=1
    elif len(str(df.iloc[i,5]))!=16:
        aber+=1
    elif any(x in df.iloc[i, 5] for x in lettre):
        aber+=1
    elif str(df.iloc[i,6])=='nan':
        miss+=1
    elif str(df.iloc[i,7])=='nan':
        miss+=1
    elif int(df.iloc[i,7])<0:
        aber+=1
    elif str(df.iloc[i,8])=='nan':
        miss+=1
    elif int(df.iloc[i,8])<0:
        aber+=1
    elif str(df.iloc[i,9])=='nan':
        miss+=1
    elif int(df.iloc[i,9])<0:
        aber+=1
    elif str(df.iloc[i,10])=='nan':
        miss+=1
    elif int(df.iloc[i,10])<0:
        aber+=1
    elif str(df.iloc[i,11])=='nan':
        miss+=1
    elif str(df.iloc[i,12])=='nan':
        miss+=1
    elif str(df.iloc[i,12])=='VRAI' and str(df.iloc[i,12])=='FAUX':
        aber+=1
    elif str(df.iloc[i,13])=='nan':
        miss+=1
    elif str(df.iloc[i,13])!='FAUX' and str(df.iloc[i,13])!='VRAI':
        aber+=1
    elif str(df.iloc[i,14])=='nan':
        miss+=1
    elif str(df.iloc[i,14])!='FAUX' and str(df.iloc[i,14])!='VRAI':
        aber+=1
print('Il y a un total de {} valeurs manquantes sur 46732 lignes, et un total de {} valeurs aberrantes sur 46732 lignes'.format(miss,aber))
print('En pourcentage ça donne {} % de valeurs manquantes et {} % de valeurs aberrantes'.format(round(pourcentage(miss),2),round(pourcentage(aber),2)))