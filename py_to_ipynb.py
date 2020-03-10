#!/usr/bin/env python
# coding: utf-8

# In[8]:


import json
import re


# In[9]:


# Here is the initial dictionary to be jsonified. Change parameters according to your ipynb settings.
initial_dict = {"cells":[],
                "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}


# In[10]:


filename = str(input('Please give the name of the .py file to be parsed to ipynb\n'))


# In[11]:


filestr = open(filename,'r').read()


# In[12]:


file_split = re.split('# In\[.*?\]:', filestr)


# In[13]:


for line in file_split:
    initial_dict['cells'].append({
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [line]
  })


# In[18]:


with open(filename+'.ipynb', 'w') as outfile:
    json.dump(initial_dict, outfile)

