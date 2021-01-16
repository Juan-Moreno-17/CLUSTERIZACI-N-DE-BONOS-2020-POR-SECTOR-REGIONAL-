#!/usr/bin/env python
# coding: utf-8

# #**BONO COVID (J)**

# In[34]:


import pandas as pd


# In[35]:


bono_cov=pd.read_csv("Bono_covid.csv", sep=';' , encoding='latin-1')


# In[36]:


bono_cov.head()


# In[37]:


bono_cov["CO_HOGAR"].value_counts()


# In[38]:


bono_cov["UBIGEO"].value_counts()


# In[39]:


bono_cov["DE_GENERO"]=bono_cov["DE_GENERO"].fillna(0)
bono_cov["DE_GENERO"]=bono_cov["DE_GENERO"].astype(int).astype(str)


# In[40]:


bono_cov["CO_RESTRI"].value_counts().index


# In[41]:


bono_cov.loc[(bono_cov["CO_RESTRI"]=='  ') | (bono_cov["CO_RESTRI"]==' '),"CO_RESTRI"]="NN"


# In[42]:


bono_cov["CO_RESTRI"].value_counts()


# In[43]:



bono_cov["FLAG_PADRON_OLD"]=bono_cov["FLAG_PADRON_OLD"].fillna(2)
bono_cov["FLAG_PADRON_OLD"]=bono_cov["FLAG_PADRON_OLD"].astype(int).astype(str)


# In[44]:


bono_cov["FLAG_PADRON_OLD"].value_counts()


# In[45]:


bono_cov["FLAG_DISCAP_SEVERA"].value_counts()


# In[46]:


bono_cov["FLAG_DISCAP_SEVERA"]=bono_cov["FLAG_DISCAP_SEVERA"].fillna(2)
bono_cov["FLAG_DISCAP_SEVERA"]=bono_cov["FLAG_DISCAP_SEVERA"].astype(int).astype(str)


# In[47]:


bono_cov["FLAG_DISCAP_SEVERA"].value_counts()


# In[48]:


bono_cov["FLAG_MAYEDAD"].value_counts()


# In[49]:


bono_cov["FLAG_MAYEDAD"]=bono_cov["FLAG_MAYEDAD"].astype(int).astype(str)


# In[58]:


bono_cov2=bono_cov.drop(bono_cov.columns[[6, 6]], axis='columns')


# In[60]:


bono_cov2.to_csv("bono.csv",index= False )


# In[ ]:




