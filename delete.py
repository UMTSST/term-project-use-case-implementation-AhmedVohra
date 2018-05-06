
# coding: utf-8

# In[132]:


fhand = open (r"C:\Users\ahmed\Desktop\book.txt")
Bname=list()
Aname=list()
ISBN=list()
for line in fhand:
    
    Bname, Aname,ISBN=line.split("|")
    Bname.in(0,Bname)

fhand.close()




# In[122]:


fhand = open (r"C:\Users\ahmed\Desktop\book.txt",'a')
for w in line:
    print(Bname)
fhand.close()
   

