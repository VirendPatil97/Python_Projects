#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, shutil


# In[5]:


path = r"/Users/virendpatil/Desktop/FileSorting/"


# In[13]:


file_names = os.listdir(path)


# In[8]:


folder_names = ['pdf_files','xlsx_files','ppt_files']


# In[12]:


for folder in folder_names:
    if not os.path.exists(path + folder):
        os.makedirs(path+folder)


# In[15]:


for file in file_names:
    if '.pdf' in file and not os.path.exists(path + 'pdf_files/'+ file):
        shutil.move(path+file,path+'pdf_files')
    elif '.xlsx' in file and not os.path.exists(path + 'xlsx_files/'+ file):
        shutil.move(path+file,path+'xlsx_files')
    elif '.pptx' in file and not os.path.exists(path + 'ppt_files/'+ file):
        shutil.move(path+file,path+'ppt_files')


# In[ ]:




