
# coding: utf-8

# In[6]:


f = open('births.csv','r')


# In[7]:


birth_data = f.read()


# In[8]:


split_list = birth_data.split('\n')


# In[9]:


split_new = []
for i in split_list:
    split_new.append(i.split(','))
     
        


# In[10]:


days_counts ={}
input_lst = split_new[1:len(split_new)]


# In[12]:


cntr = 0
for i in input_lst:
    day_of_week = i[3]
    births = int(i[4])
    found = day_of_week in days_counts
    if found == True:
        days_counts[day_of_week] = days_counts[day_of_week] + births
    else:
        days_counts[day_of_week] = births
print(days_counts)        
        

