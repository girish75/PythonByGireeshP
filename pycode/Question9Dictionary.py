# Q9.	Write the following program:
# Take two tuples such as t1 = (1, 2, 3), t2 = ("Jan", "Feb", "Mar"),
# and create two dictionaries and print them. The output should be as follows:
#  {1: 'Jan', 2: 'Feb', 3: 'Mar'}
# {'Jan': 1, 'Feb': 2, 'Mar': 3}


t1 = (1, 2, 3)
t2 = ("Jan", "Feb", "Mar")

Dic1={}
Dic2= {}
Dic3 ={}
Dic4 ={}
Dic1.update({t1[0]:t2[0],t1[1]:t2[1], t1[2]:t2[2] })
print(Dic1)

Dic2.update({t2[0]:t1[0],t2[1]:t1[1], t2[2]:t1[2] })
print(Dic2)


len1 = len(t1)
print(len1)

len2 = len(t2)
print(len2)
i = 0
while i < len1:
    Dic3.update({t1[i]:t2[i]})
    i+=1

print(Dic3)
j = 0
while j < len2:
    Dic4.update({t2[j]:t1[j]})
    j+=1

print(Dic4)

