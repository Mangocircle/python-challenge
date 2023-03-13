#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[6]:


with open ('Resources/election_data.csv',encoding='utf') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader)
    Data=[]
    votecount=0
    Candidates=set()
    Votes={}
    for rows in csvreader:
        Data.append(rows)
        votecount+=1
        name=rows[2]
        if name not in Votes:
            Votes[name]=1
        else:
            Votes[name]+=1
        Candidates.add(str(name))
        winner=max(Votes,key=Votes.get)
    Ucandi=list(Candidates)
    print(Ucandi)


# In[7]:


#assignments for output
cvotes=str(Votes[Ucandi[0]])
rvotes=str(Votes[Ucandi[1]])
dvotes=str(Votes[Ucandi[2]])
cper=str(round(int(cvotes)/votecount*100,3))+"%"
rper=str(round(int(rvotes)/votecount*100,3))+"%"
dper=str(round(int(dvotes)/votecount*100,3))+"%"


# In[8]:


#terminal output
print('Election Results')
print('----------------')
print('Total Votes: '+ str(votecount))
print(Ucandi[0]+':'+' '+cper+' | '+cvotes)
print(Ucandi[1]+':'+' '+rper+' | '+rvotes)
print(Ucandi[2]+':'+' '+dper+' | '+dvotes)
print('----------------')
print('Winner: '+winner)
print('----------------')


# In[9]:


#text file output
f=open("Results.txt","w")
f.write("Election Results"+'\n'+'\n'+"----------------------------"+'\n'+'\n')
f.write('Total Votes: '+ str(votecount)+'\n')
f.write(Ucandi[0]+':'+' '+cper+' | '+cvotes+'\n')
f.write(Ucandi[1]+':'+' '+rper+' | '+rvotes+'\n')
f.write(Ucandi[2]+':'+' '+dper+' | '+dvotes+'\n'+'\n')
f.write('----------------'+'\n'+'\n')
f.write('Winner: '+winner+'\n'+'\n')
f.write('----------------')
f.close()

