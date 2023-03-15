#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pyttsx3


# In[9]:


import PyPDF2


# In[13]:


hikaye = open("deep-learning.pdf","rb")


# In[12]:


pdfOkuyucu = PyPDF2.PdfFileReader(hikaye)


# In[14]:


from PyPDF2 import PdfReader


# In[16]:


pdfOkuyucu = PyPDF2.PdfReader(hikaye)


# In[18]:


engine = pyttsx3.init()


# In[19]:


voices = engine.getProperty('voices')


# In[20]:


engine.setProperty('voice',voices[0].id)


# In[31]:


for sayfa_numarasi in range(0,len(pdfOkuyucu.pages)):
    sayfa = pdfOkuyucu.pages[sayfa_numarasi]
    yazi = sayfa.extract_text
    engine.say(yazi)
    engine.runAndWait()


# In[ ]:




