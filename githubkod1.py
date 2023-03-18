#!/usr/bin/env python
# coding: utf-8

# In[13]:


# AÇIKLIK AÇISI HESAPLAMA
import math

x1 = 4559135.297 
y1 = 408795.699

x2 = 4559094.783
y2 = 408891.699  

arctan = math.atan((y2-y1)/(x2-x1))*200/math.pi

print("Arctanjant:", round(arctan,3))
print("Dy:",round(y2-y1,3))
print("Dx:",round(x2-x1,3))
print("Dy/Dx:", round((y2-y1)/(x2-x1),3))

if (y2-y1)>0 and (x2-x1)>0:
    print("Açıklık açısı:", round(arctan,3))
if (y2-y1)>0 and (x2-x1)<0: 
    print("Açıklık açısı:", round(arctan+200,3))
if (y2-y1)<0 and (x2-x1)<0: 
    print("Açıklık açısı:", round(arctan+200,3))
if (y2-y1)<0 and (x2-x1)>0:
    print("Açıklık açısı:" , round(arctan+400,3))


# In[ ]:




