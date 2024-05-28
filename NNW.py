#!/usr/bin/env python
# coding: utf-8

# In[1]:


def NNW(entry):
    import joblib
    from sklearn.neural_network import MLPClassifier
    import numpy as np
    red = joblib.load('C:/Users/cseba/OneDrive/Escritorio/Kaleb Red/MNIST_CLASSIFIER.pb')
    out = red.predict([entry])
    out = out[0]
    return out



# In[ ]:




