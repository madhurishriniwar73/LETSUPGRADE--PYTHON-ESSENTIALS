#!/usr/bin/env python
# coding: utf-8

# # LIST AND IT'S METHODS

# In[2]:


lst=[21,77,98,[1,2,3],'Rio','tokyo']


# In[3]:


lst


# In[6]:


lst.count(98)


# In[7]:


lst.append("Madhu")


# In[8]:


lst


# In[11]:


lst


# In[12]:


lst[3][2]


# In[13]:


lst[2][1]


# In[14]:


lst.pop(2)


# In[16]:


lst.index('Rio')


# In[17]:


lst.clear()


# In[18]:


lst


# # DICTIONARIES AND ITS METHODS

# In[20]:


dict={ 'name':"madhu",'age':18,'rollno':2273,'skill':'python'}


# In[21]:


dict


# In[23]:


dict['name']


# In[28]:


dict.get('age')


# In[29]:


dict.pop('rollno')


# In[30]:


dict


# In[36]:


type(dict)


# In[37]:


print(len(dict))


# In[40]:


dict.keys()


# In[42]:


dict.values()


# In[43]:


dict.clear()


# In[44]:


dict


# # Set and It's Methods

# In[46]:


st={'madhuri','bhagyesh',1,2,2,4,4,4,76}


# In[47]:


st


# In[48]:


st.intersection()


# In[49]:


st.discard(76)


# In[50]:


st


# In[52]:


st1={'madhuri','madhu',1,2,2,3,4}


# In[53]:


st1


# In[54]:


st.difference(st1)


# In[55]:


st1.issubset(st)


# In[56]:


st1.isdisjoint(st)


# In[57]:


type(st)


# In[58]:


st.union(st1)


# # Tuple And It's Methods

# In[61]:


#ordered immutable data type


# In[59]:


tp=1,3,'rio','raquel'


# In[60]:


tp


# In[62]:


type(tp)


# In[63]:


tp.count('rio')


# In[64]:


tp.index(3)


# # STRING AND IT'S METHODS

# In[65]:


str1='Madhuri'


# In[66]:


str2='Shriniwar'


# In[67]:


str1+str2


# In[68]:


str1.lower()


# In[69]:


str1.upper()


# In[74]:


str2[2:4]


# In[75]:


str1.split()


# In[79]:


print(len(str1))


# In[ ]:




