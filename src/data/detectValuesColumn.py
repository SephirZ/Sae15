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
print('Analyse de la variable "video_id"')
for i in range(len(df)):
    if str(df.iloc[i,0])=='nan':
        miss+=1
    elif len(str(df.iloc[i,0]))!=11:
        aber+=1
#Moyenne Valeur aberrante:
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "video_id" ce qui représente environ {} %'.format(miss, round(pourcentage(miss),2)))
    miss=0
print('Il y a {} valeur(s) aberrante(s) sur le total des valeurs "video_id" ce qui représente environ {} %'.format(aber,round(pourcentage(aber))))
aber=0

print('Analyse de la variable "trending_date"')
for i in range(len(df)):
    if str(df.iloc[i,1])=='nan':
        miss+=1
    elif len(str(df.iloc[i,1]))!=8:
        aber+=1
    elif any(x in df.iloc[i,1] for x in lettre):
        aber+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "trending_date" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il y a {} valeur(s) aberrante(s) sur le total des valeurs "trending_date" ce qui représente environ {} %'.format(aber,round(pourcentage(aber))))
aber=0


print('Analyse de la variable "title"')
for i in range(len(df)):
    if str(df.iloc[i,2])=='nan':
        miss+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "title" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il ne peut pas y avoir de valeur aberrante')

print('Analyse de la variable "channel_title"')
for i in range(len(df)):
    if str(df.iloc[i,3])=='nan':
        miss+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "channel_title" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il ne peut pas y avoir de valeur aberrante')
aber=0

print('Analyse de la variable "category_id"')
for i in range(len(df)):
    if str(df.iloc[i,4])=='nan':
        miss+=1
    elif not any(x in str(df.iloc[i,4]) for x in catID):
        aber+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "category_id" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il y a {} valeur(s) aberrante(s) sur le total des valeurs "category_id" ce qui représente environ {} %'.format(aber,round(pourcentage(aber))))
aber=0

print('Analyse de la variable "publish_time"')
for i in range(len(df)):
    if str(df.iloc[i,5])=='nan':
        miss+=1
    elif len(str(df.iloc[i,5]))!=16:
        aber+=1
    elif any(x in df.iloc[i, 5] for x in lettre):
        aber+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "publish_time" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il y a {} valeur(s) aberrante(s) sur le total des valeurs "publish_time" ce qui représente environ {} %'.format(aber,round(pourcentage(aber))))
aber=0

print('Analyse de la variable "tags"')
for i in range(len(df)):
    if str(df.iloc[i,6])=='nan':
        miss+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "tags" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il ne peut pas y avoir de valeur aberrante')

print('Analyse de la variable "views"')
for i in range(len(df)):
    if str(df.iloc[i,7])=='nan':
        miss+=1
    elif int(df.iloc[i,7])<0:
        aber+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "views" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il y a {} valeur(s) aberrante(s) sur le total des valeurs "views" ce qui représente environ {} %'.format(aber,round(pourcentage(aber))))
aber=0

print('Analyse de la variable "likes"')
for i in range(len(df)):
    if str(df.iloc[i,8])=='nan':
        miss+=1
    elif int(df.iloc[i,8])<0:
        aber+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "likes" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il y a {} valeur(s) aberrante(s) sur le total des valeurs "likes" ce qui représente environ {} %'.format(aber,round(pourcentage(aber))))
aber=0

print('Analyse de la variable "dislikes"')
for i in range(len(df)):
    if str(df.iloc[i,9])=='nan':
        miss+=1
    elif int(df.iloc[i,9])<0:
        aber+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "dislikes" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il y a {} valeur(s) aberrante(s) sur le total des valeurs "dislikes" ce qui représente environ {} %'.format(aber,round(pourcentage(aber))))
aber=0

print('Analyse de la variable "comment_count"')
for i in range(len(df)):
    if str(df.iloc[i,10])=='nan':
        miss+=1
    elif int(df.iloc[i,10])<0:
        aber+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "comment_count" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il y a {} valeur(s) aberrante(s) sur le total des valeurs "comment_count" ce qui représente environ {} %'.format(aber,round(pourcentage(aber))))
aber=0

print('Analyse de la variable "thumbnail_link"')
for i in range(len(df)):
    if str(df.iloc[i,11])=='nan':
        miss+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "thumbnail_link" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il ne peut pas y avoir de valeurs aberrantes')

print('Analyse de la variable "comments_disabled"')
for i in range(len(df)):
    if str(df.iloc[i,12])=='nan':
        miss+=1
    elif str(df.iloc[i,12])=='VRAI' and str(df.iloc[i,12])=='FAUX':
        aber+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "comments_disabled" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il y a {} valeur(s) aberrante(s) sur le total des valeurs "comment_disabled" ce qui représente environ {} %'.format(aber,round(pourcentage(aber))))
aber=0

print('Analyse de la variable "ratings_disabled"')
for i in range(len(df)):
    if str(df.iloc[i,13])=='nan':
        miss+=1
    elif str(df.iloc[i,13])!='FAUX' and str(df.iloc[i,13])!='VRAI':
        aber+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "ratings_disabled" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il y a {} valeur(s) aberrante(s) sur le total des valeurs "ratings_disabled" ce qui représente environ {} %'.format(aber,round(pourcentage(aber))))
aber=0

print(str(df.iloc[9,12]))

print('Analyse de la variable "video_error"')
for i in range(len(df)):
    if str(df.iloc[i,14])=='nan':
        miss+=1
    elif str(df.iloc[i,14])!='FAUX' and str(df.iloc[i,14])!='VRAI':
        aber+=1
if miss==0:
    print('Il n\'y a aucune valeur manquante.')
else:
    print('Il y a {} valeur(s) manquante(s) sur le total des valeurs de "video_error" ce qui représente environ {} %'.format(miss, round(pourcentage(miss))))
    miss=0
print('Il y a {} valeur(s) aberrante(s) sur le total des valeurs "video_error" ce qui représente environ {} %'.format(aber,round(pourcentage(aber))))