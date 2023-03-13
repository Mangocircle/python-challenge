#!/usr/bin/env python
# coding: utf-8

# In[123]:


import os
import csv


# In[124]:


with open('C:/Users/Henry/Desktop/Class/Homework/Python Challenge(1)/python-challenge/PyBank/Resources/budget_data.csv',encoding='utf') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader)
    rowcount=0
    ploss=0
    values=[]
    cbv=[]
    Data=[]
    for row in csvreader:
        Data.append(row)
        rowcount+=1
        ploss+=int(row[1])
        values.append(int(row[1]))
    for i in range(1,len(values)):
        cbv.append(values[i]-values[(i-1)])
    def avg(numbers):
        average=(sum(numbers))/len(numbers)
        return average
    cbva=round(avg(cbv),2)
    maxi=max(cbv)
    mini=min(cbv)

    for x in range(len(cbv)):
        if mini == cbv[x]:
                     #   V skipped header row and added one to skip initial empty value
            Gdec=(Data[x+1][0]+" "+"$"+str(cbv[x]))
        if maxi == cbv[x]:
                     #   V skipped header row and added one to skip initial empty value
            Ginc=(Data[x+1][0]+" "+"$"+str(cbv[x]))


# In[125]:


print("Total Months: "+str(rowcount))
print("Total: "+"$"+str(ploss))
print("Average Change: "+"$"+str(cbva))
print("Greatest Increase in Profits: "+Ginc)
print("Greatest Decrease in Profits: "+Gdec)


# In[144]:


f=open("Results.txt","w")
f.write("Financial Analysis"+'\n'+'\n'+"----------------------------"+'\n'+'\n')
f.write("Total Months: "+str(rowcount)+'\n')
f.write("Total: "+"$"+str(ploss)+'\n')
f.write("Average Change: "+"$"+str(cbva)+'\n')
f.write("Greatest Increase in Profits: "+Ginc+'\n')
f.write("Greatest Increase in Profits: "+Gdec+'\n')
f.close()


# In[ ]:




