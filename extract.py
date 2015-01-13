import csv
import numpy as np
from math import sqrt
reader=csv.reader(open("sam3.csv","r"),delimiter='\t',quoting=csv.QUOTE_NONE)
header=reader.next()
songs_dict={}
song_dict={}
song_count={}
set_userid=set([])
set_artist=set([])
set_track=set([])
list1=[]

for row in reader:
	list1.append(dict(zip(header,row)))

#print list1[1]

header2=['user_id','art_name','tra_name']
list2=[]

for item in list1:
	if item['userid']!='' and \
           item['artname']!='' and \
           item['traname']!='':
		list2.append(dict(zip(header2,[item['userid'],item['artname'],item['traname']])))

for  item in list2:
	set_userid.add(item['user_id'])
	set_artist.add(item['art_name'])
	set_track.add(item['tra_name'])

for item in set_userid:
	songs_dict[item]={}
	song_dict[item]={}
	song_count[item]={}

for item in list2:
	songs_dict[item['user_id']].update({item['tra_name']:item['art_name']})


#for item in set_userid:
for item in list2:
	song_dict[item['userid']].update({item['traname']})



def song_count(song,userlist,userid):
	count=0
	for item2 in userlist:
		if item2['user_id']==userid and item2['tra_name']==song:
			count+=1
    
return count

for item in set_userid:
	for item1 in set_track:
		c=song_count(item1,list3,item)
        song_dict[item].update({item1:c}) 

#for item in song_dict:
 #        print song_dict[item]
